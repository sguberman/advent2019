from itertools import zip_longest
from typing import Callable, Dict, List, Tuple


def program_add(program: List[str], a: int, b: int, address: int) -> List[str]:
    """
    Opcode: 1
    Add a and b, storing the result in the given address in program.
    Return the program.
    """
    program[address] = str(a + b)
    return program


def program_mul(program: List[str], a: int, b: int, address: int) -> List[str]:
    """
    Opcode: 2
    Multiply a and b, storing the result in the given address in program.
    Return the program.
    """
    program[address] = str(a * b)
    return program


def program_inp(program: List[str], address: int) -> List[str]:
    """
    Opcode: 3
    Get an integer test ID as input from the user. Store it at the given
    address in the program. Return the program.
    """
    while True:
        input_id = input('Enter integer ID: ')
        try:
            int(input_id)
            break
        except ValueError as e:
            print(e)
            print('Invalid input, must be integer. Try again.')
    program[address] = input_id
    return program


def program_out(program: List[str], value: int) -> List[str]:
    """
    Opcode: 4
    Print the provided value. Return the program.
    """
    print('DIAGNOSTIC: ', value)
    return program


num_params: Dict[int, int] = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    99: 0
}

operations: Dict[int, Callable] = {
    1: program_add,
    2: program_mul,
    3: program_inp,
    4: program_out,
}


def parse_input(inputfile: str) -> List[str]:
    """
    Parse the puzzle input file, returning a list of str intcodes.
    """
    return [x for x in open(inputfile).read().split(',')]


def parse_opvalue(opvalue: str) -> Tuple[int, ...]:
    """
    Parse the first value of an instruction, returning a tuple of the opcode
    and parameter modes as ints.
    """
    opcode = int(opvalue[-2:])
    modes: List[int] = [
        int(x)
        for x, _ in zip_longest(opvalue[-3::-1],
                                range(num_params[opcode]),
                                fillvalue=0)]
    if modes and (opcode != 4):  # destination address is always immediate mode
        modes[-1] = 1
    return opcode, *modes


def parse_parameters(
        program: List[str],
        pointer: int,
        modes: List[int]) -> List[int]:
    """
    Parse the parameters for an instruction beginning at instruction_pointer
    using the provided parameter modes.
    """
    parameters = []
    for mode, value in zip(modes, program[pointer + 1:]):
        if mode == 0:  # position mode
            parameter = int(program[int(value)])
        elif mode == 1:  # immediate mode
            parameter = int(value)
        parameters.append(parameter)
    return parameters


def step(program: List[str], pointer: int = 0) -> List[str]:
    """
    Execute the instruction at the given position in the program. Continue
    calling step until reaching opcode 99 and halt the program, returning the
    final state of memory.
    """
    opcode, *modes = parse_opvalue(program[pointer])
    if opcode == 99:  # halt
        return program
    else:
        op = operations[opcode]
        args = parse_parameters(program, pointer, modes)
        program = op(program, *args)
        pointer += len(args) + 1
        return step(program, pointer)


def part1(inputfile: str) -> List[str]:
    """
    After providing 1 to the only input instruction and passing all the tests,
    what diagnostic code does the program produce?
    """
    program = parse_input(inputfile)
    memory = step(program)
    return memory


if __name__ == '__main__':
    part1('input_day05.txt')
