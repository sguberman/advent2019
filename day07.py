from itertools import permutations
from typing import Callable, List, Iterable, Tuple

from intcode import Computer


def max_thrust(
        amps: List[Computer],
        phases: Iterable[int]) -> Tuple[int, Tuple[int, ...]]:
    '''
    Find the max thrust by varying the phase setting on each amp.
    Return the max thrust and corresponding sequence of settings in a tuple.
    '''
    return max((thrust(amps, settings), settings)
               for settings in permutations(phases))


def thrust(
        amps: List[Computer],
        phase_settings: Tuple[int, ...],
        log_output: bool = False) -> int:
    '''
    Compute the thrust signal provided by the amps with the given settings.
    '''
    if (amp_len := len(amps)) != (phase_len := len(phase_settings)):
        raise ValueError(f'Length of amps ({amp_len}) and ' +
                         f'phase_settings ({phase_len}) must match.')
    for amp in amps:
        amp.initialize_memory()  # reset program memory, pointer, and outputs
    amp_input: int = 0
    for amp, phase_setting in zip(amps, phase_settings):
        amp_output = amp.run(with_inputs=[phase_setting, amp_input],
                             stop_at_first_output=True,
                             log_output=log_output)
        amp_input = amp_output[0]
    return amp_output[0]


def amp_series(
        num_amps: int,
        program: str,
        from_file: bool = True) -> List[Computer]:
    '''
    Build a series of amps with software defined by the given program.
    '''
    if from_file:
        Constructor: Callable = Computer.from_file
    else:
        Constructor = Computer.from_text
    return [Constructor(program) for _ in range(num_amps)]


def part1(inputfile: str) -> int:
    '''
    What is the highest signal that can be sent to the thrusters?
    '''
    amps = amp_series(5, inputfile)
    phases = range(len(amps))
    thrust, _ = max_thrust(amps, phases)
    return thrust


if __name__ == '__main__':
    print(part1('input_day07.txt'))
