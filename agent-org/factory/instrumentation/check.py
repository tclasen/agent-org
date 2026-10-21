#!/usr/bin/env python3
"""Validate formal Markdown records. Exit 1 preserves failing quality-gate status."""
import argparse
import json
try:
    from .records import validate_tree
except ImportError:
    from records import validate_tree


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True)
    args = parser.parse_args()
    result = validate_tree(args.root)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result['valid'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
