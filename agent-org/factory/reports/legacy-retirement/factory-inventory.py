"""Read-only inventory and hash dedup; never imports or runs source code.

Run from /Users/Shared with Python 3. Writes only factory-* artifacts beside self.
All regular file paths/size recorded; dependency, Git object, large media payloads
are explicitly not content-reviewed. Symlinks are recorded without following.
"""
import collections, hashlib, json, os, pathlib, stat

BASE = pathlib.Path('/Users/Shared')
OUT = BASE / 'agent-org/factory/reports/legacy-retirement'
ROOTS = ['old/factory', 'old/work', 'old/agent-collaboration', 'old/agent-handoffs',
         'old/factory-eval-workspaces', 'old/factory-evals-workspaces']
DEPENDENCY = {'node_modules', '.venv', 'venv', '__pycache__', '.next', '.mypy_cache', '.ruff_cache', '.pytest_cache', '.cache'}
summary = {}
groups = collections.defaultdict(list)
errors = []
with (OUT / 'factory-files.jsonl').open('w') as manifest:
  for root in ROOTS:
    counts = collections.Counter()
    classes = collections.Counter()
    def fail(err):
      errors.append({'path': str(err.filename), 'error': type(err).__name__})
    for directory, dirs, files in os.walk(BASE / root, followlinks=False, onerror=fail):
      dirs.sort(); files.sort()
      for name in dirs[:]:
        p = pathlib.Path(directory) / name
        if p.is_symlink():
          files.append(name); dirs.remove(name)
      for name in files:
        p = pathlib.Path(directory) / name
        rel = str(p.relative_to(BASE))
        row = {'path': rel}
        try:
          info = p.lstat()
          row['bytes'] = info.st_size
          counts['entries'] += 1; counts['bytes'] += info.st_size
          parts = p.parts
          if stat.S_ISLNK(info.st_mode):
            row['class'] = 'symlink-not-followed'; row['target'] = os.readlink(p)
          elif not stat.S_ISREG(info.st_mode):
            row['class'] = 'special-not-read'
          elif '.git' in parts:
            row['class'] = 'git-metadata-not-reviewed'
          elif any(part in DEPENDENCY for part in parts):
            row['class'] = 'dependency-cache-not-reviewed'
          elif info.st_size > 20 * 1024 * 1024:
            row['class'] = 'large-payload-not-reviewed'
          else:
            data = p.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            row['sha256'] = digest
            row['class'] = 'hashed-text' if b'\0' not in data[:8192] else 'hashed-binary'
            groups[digest].append(rel)
            counts['hashed'] += 1
          classes[row['class']] += 1
        except OSError as err:
          row['class'] = 'unreadable'; row['error'] = type(err).__name__
          classes['unreadable'] += 1
          errors.append({'path': rel, 'error': type(err).__name__})
        manifest.write(json.dumps(row, sort_keys=True) + '\n')
    summary[root] = {'counts': dict(counts), 'classes': dict(classes)}
with (OUT / 'factory-hash-groups.jsonl').open('w') as output:
  for digest, paths in sorted(groups.items()):
    output.write(json.dumps({'sha256': digest, 'paths': paths}, sort_keys=True) + '\n')
result = {'roots': summary, 'errors': errors, 'unique_hashes': len(groups), 'method': 'factory-inventory.py; SHA-256; sorted os.walk including hidden/ignored; no symlink traversal; no legacy execution; exclusions explicit per path'}
(OUT / 'factory-inventory-summary.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
print(json.dumps(result, indent=2, sort_keys=True))
