#!/usr/bin/env python3
"""Illustrative horizontal two-link gravity estimate; never commands hardware."""
import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def calculate(c):
    keys = (
        'gravity_m_s2', 'upper_length_m', 'forearm_length_m',
        'upper_link_mass_kg', 'forearm_link_mass_kg', 'elbow_module_mass_kg',
        'wrist_modules_mass_kg', 'distal_load_mass_kg',
        'distal_load_com_beyond_wrist_m', 'reserve_multiplier',
    )
    for key in keys:
        value = c[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f'{key} must be numeric')
        if not math.isfinite(value) or value < 0:
            raise ValueError(f'{key} must be finite and nonnegative')
    if min(c['upper_length_m'], c['forearm_length_m'], c['gravity_m_s2']) <= 0:
        raise ValueError('Lengths and gravity must be positive')
    if c['reserve_multiplier'] < 1:
        raise ValueError('reserve_multiplier must be >= 1')
    a, b = c['upper_length_m'], c['forearm_length_m']
    g, d = c['gravity_m_s2'], c['distal_load_com_beyond_wrist_m']
    shoulder = g * (
        c['upper_link_mass_kg'] * a / 2
        + c['elbow_module_mass_kg'] * a
        + c['forearm_link_mass_kg'] * (a + b / 2)
        + c['wrist_modules_mass_kg'] * (a + b)
        + c['distal_load_mass_kg'] * (a + b + d)
    )
    elbow = g * (
        c['forearm_link_mass_kg'] * b / 2
        + c['wrist_modules_mass_kg'] * b
        + c['distal_load_mass_kg'] * (b + d)
    )
    return {
        'shoulder_static_output_Nm': shoulder,
        'elbow_static_output_Nm': elbow,
        'shoulder_with_reserve_Nm': shoulder * c['reserve_multiplier'],
        'elbow_with_reserve_Nm': elbow * c['reserve_multiplier'],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=ROOT / 'config/static-sizing.json')
    args = parser.parse_args()
    try:
        result = calculate(json.loads(args.config.read_text()))
    except (OSError, ValueError, KeyError) as exc:
        parser.error(str(exc))
    print('ILLUSTRATIVE STATIC OUTPUT TORQUE — NOT A MOTOR RATING')
    for key, value in result.items():
        print(f'{key}: {value:.4f}')
    print('No inertia, friction, contact, gearing, thermal or bearing validation included.')


if __name__ == '__main__':
    main()
