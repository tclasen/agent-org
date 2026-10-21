"""Explicit argument-array command capture; raw arguments/output never returned.

Timeout/output caps terminate the owned process group. This is an observation
utility, not a sandbox: callers must approve the executable, cwd and side effects.
"""
import hashlib
import os
import selectors
import signal
import subprocess
import time
from pathlib import Path
try:
    from .common import canonical, digest
except ImportError:
    from common import canonical, digest


def run_command(argv, *, cwd, timeout=30, max_output_bytes=1_000_000):
    if not isinstance(argv, list) or not argv or any(not isinstance(v, str) or '\0' in v for v in argv):
        raise ValueError('command must be a nonempty string argument array')
    if type(timeout) not in (int, float) or not 0 < timeout <= 3600:
        raise ValueError('timeout must be positive and at most one hour')
    if type(max_output_bytes) is not int or not 1 <= max_output_bytes <= 100_000_000:
        raise ValueError('invalid output bound')
    cwd = Path(cwd).resolve(strict=True)
    if not cwd.is_dir():
        raise ValueError('cwd must be a directory')
    started = time.monotonic()
    report = {'argv_sha256': digest(argv), 'cwd_sha256': hashlib.sha256(os.fsencode(cwd)).hexdigest(),
              'exit_code': None, 'duration_seconds': None, 'timed_out': False,
              'output_limit_exceeded': False, 'error_code': None}
    try:
        process = subprocess.Popen(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.DEVNULL, shell=False, start_new_session=True)
    except OSError:
        report.update(exit_code=127, duration_seconds=time.monotonic() - started, error_code='spawn_failed')
        report.update(stdout_bytes=0, stderr_bytes=0, stdout_sha256=hashlib.sha256(b'').hexdigest(), stderr_sha256=hashlib.sha256(b'').hexdigest())
        return report
    hashes = {name: hashlib.sha256() for name in ('stdout', 'stderr')}
    sizes = {'stdout': 0, 'stderr': 0}
    selector = selectors.DefaultSelector()
    selector.register(process.stdout, selectors.EVENT_READ, 'stdout')
    selector.register(process.stderr, selectors.EVENT_READ, 'stderr')
    killed = False
    try:
        while selector.get_map():
            if time.monotonic() - started >= timeout and not killed:
                report['timed_out'] = True
                killed = True
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            # Descendants cannot hold pipes forever after the capture bound.
            if killed:
                for key in list(selector.get_map().values()):
                    selector.unregister(key.fileobj)
                    key.fileobj.close()
                break
            for key, _ in selector.select(min(0.05, max(0, timeout - (time.monotonic() - started)))):
                chunk = os.read(key.fd, 65536)
                if not chunk:
                    selector.unregister(key.fileobj)
                    key.fileobj.close()
                    continue
                name = key.data
                hashes[name].update(chunk)
                sizes[name] += len(chunk)
                if sum(sizes.values()) > max_output_bytes:
                    report['output_limit_exceeded'] = True
                    killed = True
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    break
        remaining = max(0.001, timeout - (time.monotonic() - started))
        try:
            report['exit_code'] = process.wait(timeout=remaining)
        except subprocess.TimeoutExpired:
            report['timed_out'] = True
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            report['exit_code'] = process.wait(timeout=5)
    finally:
        selector.close()
        for stream in (process.stdout, process.stderr):
            stream.close()
        if process.poll() is None:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.wait(timeout=5)
    report['duration_seconds'] = time.monotonic() - started
    for name in hashes:
        report[name + '_sha256'] = hashes[name].hexdigest()
        report[name + '_bytes'] = sizes[name]
    return report
