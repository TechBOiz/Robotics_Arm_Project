#!/usr/bin/env python3
"""Validate project-planning IDs and references, without external dependencies."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT / path).read_text())


def unique(items, key):
    values = [item[key] for item in items]
    if len(set(values)) != len(values):
        raise ValueError(f'Duplicate {key}: {values}')
    return set(values)


def main():
    milestones = read('planning/milestones.json')
    issues = read('planning/issues.json')
    labels = read('planning/labels.json')
    bom = read('bom/items.json')
    mids = unique(milestones, 'id')
    iids = unique(issues, 'id')
    names = unique(labels, 'name')
    unique(bom, 'id')
    graph = {}
    for issue in issues:
        if issue['milestone'] not in mids:
            raise ValueError(f"Unknown milestone for {issue['id']}")
        if not set(issue['labels']) <= names:
            raise ValueError(f"Unknown labels for {issue['id']}")
        if not set(issue['depends_on']) <= iids:
            raise ValueError(f"Unknown dependency for {issue['id']}")
        if not issue['acceptance']:
            raise ValueError(f"Missing acceptance for {issue['id']}")
        graph[issue['id']] = issue['depends_on']
    done, visiting = set(), set()

    def visit(node):
        if node in visiting:
            raise ValueError('Cyclic issue dependencies')
        if node in done:
            return
        visiting.add(node)
        for dependency in graph[node]:
            visit(dependency)
        visiting.remove(node)
        done.add(node)

    for node in graph:
        visit(node)
    for item in bom:
        if item['status'] != 'unselected':
            raise ValueError('Initial BOM must not silently mark items selected')
        if item['unit_price'] is not None or item['part_number'] is not None:
            raise ValueError('Initial BOM contains an unexpected part/price')
    print(f'PASS: {len(milestones)} milestones, {len(issues)} issues, '
          f'{len(labels)} labels, {len(bom)} BOM categories; dependencies acyclic.')


if __name__ == '__main__':
    main()
