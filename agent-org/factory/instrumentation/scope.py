"""Explicit scope checks and bounded snapshots; these are not tool interception."""
import hashlib
import os
import subprocess
from pathlib import Path
try:
    from .common import digest
except ImportError:
    from common import digest


def resolve_scoped_path(root, relative, allowed=('.',)):
    root = Path(root).resolve(strict=True)
    raw = Path(relative)
    if raw.is_absolute() or '..' in raw.parts:
        raise ValueError('absolute paths and traversal are forbidden')
    candidate = (root / raw).resolve()
    if not candidate.is_relative_to(root):
        raise ValueError('symlink escapes root')
    scopes = []
    for item in allowed:
        scope = Path(item)
        if scope.is_absolute() or '..' in scope.parts:
            raise ValueError('invalid allowed scope')
        resolved = (root / scope).resolve()
        if not resolved.is_relative_to(root):
            raise ValueError('allowed scope escapes root')
        scopes.append(resolved)
    if not any(candidate == item or candidate.is_relative_to(item) for item in scopes):
        raise ValueError('path outside authorized scope')
    return candidate


def snapshot_tree(root, *, exclude=(), max_files=10000, max_bytes=100_000_000):
    """Caller names a small safe evidence root/exclusions; symlinks never followed.

    Symlink targets are hashed, not persisted; special files are rejected. Git
    directories are excluded by default, including nested Git directories.
    """
    root = Path(root).resolve(strict=True)
    if max_files < 1 or max_bytes < 0:
        raise ValueError('invalid snapshot limits')
    exclusions = tuple(sorted(set(('.git',) + tuple(exclude))))
    files, total = {}, 0
    for current, dirs, names in os.walk(root, followlinks=False):
        base = Path(current)
        for name in sorted(dirs + names):
            path = base / name
            rel = path.relative_to(root).as_posix()
            if any(rel == ex or rel.startswith(ex.rstrip('/') + '/') or name == '.git' for ex in exclusions):
                if name in dirs:
                    dirs.remove(name)
                continue
            if path.is_symlink():
                target = os.readlink(path)
                resolved = path.resolve()
                if not resolved.is_relative_to(root):
                    raise ValueError('snapshot symlink escapes root')
                files[rel] = {'kind': 'symlink', 'sha256': hashlib.sha256(os.fsencode(target)).hexdigest()}
                if name in dirs:
                    dirs.remove(name)
            elif path.is_file():
                hasher, size = hashlib.sha256(), 0
                with path.open('rb') as stream:
                    for chunk in iter(lambda: stream.read(65536), b''):
                        size += len(chunk)
                        total += len(chunk)
                        if total > max_bytes:
                            raise ValueError('snapshot byte limit exceeded')
                        hasher.update(chunk)
                files[rel] = {'kind': 'file', 'size': size, 'sha256': hasher.hexdigest(), 'executable': bool(path.stat().st_mode & 0o111)}
            elif not path.is_dir():
                raise ValueError('snapshot special file unsupported')
            if len(files) > max_files:
                raise ValueError('snapshot file limit exceeded')
        dirs.sort()
    content = {'schema_version': 1, 'files': files, 'exclusions': list(exclusions)}
    return {**content, 'snapshot_hash': digest(content), 'trusted_anchor': None}


def verify_snapshot(snapshot):
    content = {key: value for key, value in snapshot.items() if key not in {'snapshot_hash', 'trusted_anchor'}}
    if digest(content) != snapshot.get('snapshot_hash'):
        raise ValueError('snapshot hash mismatch')
    return True


def compare_snapshots(before, after, allowed=()):
    verify_snapshot(before)
    verify_snapshot(after)
    if before['exclusions'] != after['exclusions']:
        raise ValueError('snapshot evidence boundaries differ')
    changed = sorted(k for k in before['files'].keys() | after['files'].keys() if before['files'].get(k) != after['files'].get(k))
    violations = [p for p in changed if not any(p == a or p.startswith(a.rstrip('/') + '/') for a in allowed)]
    return {'changed': changed, 'violations': violations, 'boundary_preserved': not violations}


def git_provenance(root):
    """No remote URLs or file contents are returned; dirty status includes untracked."""
    def git(*args):
        result = subprocess.run(['git', '-C', str(root), *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
        return result.returncode, result.stdout
    code, top = git('rev-parse', '--show-toplevel')
    if code:
        return {'git': False, 'head': None, 'branch': None, 'trusted_anchor': None}
    _, head = git('rev-parse', '--verify', 'HEAD')
    _, branch = git('symbolic-ref', '--short', '-q', 'HEAD')
    code, status = git('status', '--porcelain=v1', '-z', '--untracked-files=all')
    if code:
        raise ValueError('git status failed')
    _, remotes = git('remote', '-v')
    # URLs may contain credentials: retain only their digest.
    return {'git': True, 'repository_identity': hashlib.sha256(top.strip()).hexdigest(),
            'head': head.decode().strip() if len(head.strip()) in (40, 64) else None,
            'branch': branch.decode().strip() or None, 'dirty': bool(status),
            'status_sha256': hashlib.sha256(status).hexdigest(),
            'remote_identity_sha256': hashlib.sha256(remotes).hexdigest(),
            'ignored_and_nested_contents': 'not observed; use explicit scoped snapshots', 'trusted_anchor': None}
