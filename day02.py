from itertools import product
from operator import add, mul
from typing import Any, Callable, Dict, List, Union


operations: Dict[int, Callable] = {
    1: add,
    2: mul,
}


def parse_input(inputfile: str) -> List[int]:
    """
    Read the puzzle input file and return a list of intcodes.
    """
    return [int(x) for x in open(inputfile).read().split(',')]


def step(program: List[int], position: int = 0) -> List[int]:
    """
    Execute the opcode at a given position in the program. Continue calling
    step until reaching opcode 99 and halt the program, returning the final
    state.
    """
    opcode = program[position]
    if opcode == 99:
        return program
    else:
        operation = operations[opcode]
        a = program[program[position+1]]
        b = program[program[position+2]]
        out = program[position+3]
        program[out] = operation(a, b)
        return step(program, position+4)


def set_inputs(program: List[int], noun: int, verb: int) -> List[int]:
    """
    Initialize the noun and verb inputs in a given program.
    """
    program[1] = noun
    program[2] = verb
    return program


def part1(inputfile: str) -> int:
    """
    Once you have a working computer, the first step is to restore the
    gravity assist program (your puzzle input) to the "1202 program alarm"
    state it had just before the last computer caught fire. To do this,
    before running the program, replace position 1 with the value 12 and
    replace position 2 with the value 2. What value is left at position 0
    after the program halts?
    """
    program = parse_input(inputfile)
    program = set_inputs(program, 12, 2)
    final_state = step(program)
    return final_state[0]


def determine_inputs(program: List[int], output: int) -> Any:
    """
    Try input nouns and verbs 0-99 inclusive until getting desired output
    from a given program. Otherwise return False.
    """
    for noun, verb in product(range(100), range(100)):
        temp_program = [x for x in program]
        initialized_program = set_inputs(temp_program, noun, verb)
        temp_output = step(initialized_program)[0]
        if temp_output == output:
            return (noun, verb)
    return False


def part2(inputfile: str) -> Union[int, str]:
    """
    Find the input noun and verb that cause the program to produce the
    output 19690720. What is 100 * noun + verb? (For example, if noun=12
    and verb=2, the answer would be 1202.)
    """
    program = parse_input(inputfile)
    result = determine_inputs(program, 19690720)
    if result:
        noun, verb = result
        return 100 * noun + verb
    else:
        return 'No Solution'


if __name__ == '__main__':
    print(part1('input_day02.txt'))
    print(part2('input_day02.txt'))
