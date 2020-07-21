import pytest
from typing import List, Tuple

import day07

programs: List[str] = [
    '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0',
    '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0',
    '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,' +
    '31,31,1,32,31,31,4,31,99,0,0,0',
]

phase_settings: List[Tuple[int, ...]] = [
    (4, 3, 2, 1, 0),
    (0, 1, 2, 3, 4),
    (1, 0, 4, 3, 2),
]

thrusts: List[int] = [
    43210,
    54321,
    65210,
]

test_data: List = list(zip(programs, phase_settings, thrusts))


@pytest.mark.parametrize('program,setting,thrust', test_data)
def test_thrust(program, setting, thrust):
    amps = day07.amp_series(5, program, from_file=False)
    assert day07.thrust(amps, setting) == thrust


@pytest.mark.parametrize('program,setting,thrust', test_data)
def test_max_thrust(program, setting, thrust):
    amps = day07.amp_series(5, program, from_file=False)
    phases = range(len(amps))
    assert day07.max_thrust(amps, phases) == (thrust, setting)


def test_part1():
    assert day07.part1('input_day07.txt') == 437860
