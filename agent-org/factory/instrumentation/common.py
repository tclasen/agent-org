"""Canonical serialization and deliberately narrow safe telemetry vocabulary."""
import hashlib
import json
import re
from datetime import datetime, timezone


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode('utf-8')


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def utc(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z', value):
        raise ValueError('timestamp must be an ISO UTC string ending Z')
    parsed = datetime.fromisoformat(value[:-1] + '+00:00')
    if parsed.utcoffset().total_seconds() != 0:
        raise ValueError('timestamp must be UTC')
    return parsed


def now():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
