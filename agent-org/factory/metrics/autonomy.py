#!/usr/bin/env python3
"""Summarize attributed autonomous-work observations; never infer missing usage.

CLI: autonomy.py OBSERVATIONS.json. Input is a JSON list of attempt observations.
No promotion decision, price lookup, task mutation or external calls occur.
"""
import argparse
import json
import math


def _number(value):
    return type(value) in (int, float) and math.isfinite(value) and value >= 0


def summarize(observations):
    if not isinstance(observations, list):
        raise ValueError('observations must be a list')
    identities, tasks = set(), {}
    outcomes = {name: 0 for name in ('accepted', 'failed', 'blocked', 'unknown')}
    bools = {name: [] for name in ('recovery_success', 'effect_reconciled_before_retry', 'lesson_recurred')}
    resources = {name: [] for name in ('active_seconds', 'tokens', 'cost_usd')}
    retries, ordinals, unknown_ordinals = 0, {}, 0
    for row in observations:
        if not isinstance(row, dict) or not all(isinstance(row.get(k), str) and row[k].strip() for k in ('attempt_id', 'task_id', 'source')):
            raise ValueError('each observation needs attempt_id, task_id and attributed source')
        if row['attempt_id'] in identities:
            raise ValueError('duplicate attempt identity')
        identities.add(row['attempt_id'])
        outcome = row.get('outcome', 'unknown')
        if outcome not in outcomes:
            raise ValueError('invalid outcome')
        number = row.get('attempt_number')
        if number is None:
            unknown_ordinals += 1
        else:
            if type(number) is not int or number < 1:
                raise ValueError('attempt_number must be a positive integer or unknown')
            observed = ordinals.setdefault(row['task_id'], set())
            if number in observed:
                raise ValueError('duplicate per-task attempt ordinal')
            observed.add(number)
            retries += number > 1
        outcomes[outcome] += 1
        tasks.setdefault(row['task_id'], []).append(outcome)
        for name, values in bools.items():
            value = row.get(name)
            if value is not None and type(value) is not bool:
                raise ValueError('invalid nullable boolean: ' + name)
            values.append(value)
        usage = row.get('resources', {})
        if not isinstance(usage, dict) or set(usage) - set(resources):
            raise ValueError('invalid resource fields')
        for name, values in resources.items():
            value = usage.get(name)
            if value is not None and (not _number(value) or (name == 'tokens' and type(value) is not int)):
                raise ValueError('invalid nonnegative resource: ' + name)
            values.append(value)
    total = len(observations)
    known = total - outcomes['unknown']
    rates = {}
    for name, values in bools.items():
        measured = [value for value in values if value is not None]
        rates[name] = {'true': sum(measured), 'known': len(measured), 'unknown': total - len(measured),
                       'total': total, 'rate': sum(measured) / len(measured) if measured else None}
    usage = {}
    for name, values in resources.items():
        measured = [value for value in values if value is not None]
        usage[name] = {'observed_sum': sum(measured) if measured else None,
                       'total': sum(measured) if total and len(measured) == total else None,
                       'known': len(measured), 'unknown': total - len(measured)}
    consistent = [rows for rows in tasks.values() if 'unknown' not in rows]
    return {'schema_version': 1, 'attempts': total, 'tasks': len(tasks), 'retry_attempts': retries if not unknown_ordinals else None,
            'observed_retry_attempts': retries, 'unknown_attempt_ordinals': unknown_ordinals,
            'outcomes': outcomes, 'accepted_rate': outcomes['accepted'] / known if known else None,
            'outcome_denominator': known, 'unknown_outcomes': outcomes['unknown'],
            'all_attempts_accepted': {'tasks': sum(all(x == 'accepted' for x in rows) for rows in consistent),
                                      'known_tasks': len(consistent), 'unknown_tasks': len(tasks) - len(consistent)},
            'reliability': rates, 'resources': usage,
            'measurement_health': {'source': 'caller-attributed observations only',
                                   'actual_model': 'unknown', 'coverage': 'unobserved operations not inferred',
                                   'promotion': 'none; prior independent evidence gate remains authoritative'}}


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key')
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('observations')
    args = parser.parse_args()
    try:
        with open(args.observations, encoding='utf-8') as stream:
            result = summarize(json.load(stream, object_pairs_hook=_unique))
        print(json.dumps(result, indent=2, allow_nan=False))
        return 0
    except (OSError, ValueError, TypeError) as error:
        print(json.dumps({'error': str(error)}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
