from itertools import zip_longest
from typing import Callable, Dict, List, Tuple


def program_add(
        program: List[str],
        pointer: int,
        a: int,
        b: int,
        address: int) -> Tuple[List[str], int]:
    """
    Opcode: 1
    Add a and b, storing the result in the given address in program.
    Return the program and pointer.
    """
    program[address] = str(a + b)
    pointer += 4
    return program, pointer


def program_mul(
        program: List[str],
        pointer: int,
        a: int,
        b: int,
        address: int) -> Tuple[List[str], int]:
    """
    Opcode: 2
    Multiply a and b, storing the result in the given address in program.
    Return the program and pointer.
    """
    program[address] = str(a * b)
    pointer += 4
    return program, pointer


def program_inp(
        program: List[str],
        pointer: int,
        address: int) -> Tuple[List[str], int]:
    """
    Opcode: 3
    Get an integer test ID as input from the user. Store it at the given
    address in the program. Return the program and pointer.
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
    pointer += 2
    return program, pointer


def program_out(
        program: List[str],
        pointer: int,
        value: int) -> Tuple[List[str], int]:
    """
    Opcode: 4
    Print the provided value. Return the program and pointer.
    """
    print('DIAGNOSTIC: ', value)
    pointer += 2
    return program, pointer


def program_jit(
        program: List[str],
        pointer: int,
        a: int,
        b: int) -> Tuple[List[str], int]:
    """
    Opcode: 5
    If a is non-zero, set the pointer to b. Return program and pointer.
    """
    if a != 0:
        pointer = b
    else:
        pointer += 3
    return program, pointer


def program_jif(
        program: List[str],
        pointer: int,
        a: int,
        b: int) -> Tuple[List[str], int]:
    """
    Opcode: 6
    If a is zero, set the pointer to b. Return the program and pointer.
    """
    if a == 0:
        pointer = b
    else:
        pointer += 3
    return program, pointer


def program_clt(
        program: List[str],
        pointer: int,
        a: int,
        b: int,
        address: int) -> Tuple[List[str], int]:
    """
    Opcode: 7
    If a is less than b, store 1 at the address in program. Otherwise store 0.
    Return the program and pointer.
    """
    if a < b:
        program[address] = str(1)
    else:
        program[address] = str(0)
    pointer += 4
    return program, pointer


def program_ceq(
        program: List[str],
        pointer: int,
        a: int,
        b: int,
        address: int) -> Tuple[List[str], int]:
    """
    If a is equal to b, store 1 at the address in program. Otherwise store 0.
    Return the program and pointer.
    """
    if a == b:
        program[address] = str(1)
    else:
        program[address] = str(0)
    pointer += 4
    return program, pointer


num_params: Dict[int, int] = {  # opcode -> num_params
    1: 3,  # add
    2: 3,  # multiply
    3: 1,  # input
    4: 1,  # output
    5: 2,  # jump-if-true
    6: 2,  # jump-if-false
    7: 3,  # less than
    8: 3,  # equals
    99: 0  # halt
}

operations: Dict[int, Callable] = {  # opcode -> function
    1: program_add,
    2: program_mul,
    3: program_inp,
    4: program_out,
    5: program_jit,
    6: program_jif,
    7: program_clt,
    8: program_ceq,
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
    # Destination address is always immediate for ops that store a value.
    if modes and (opcode not in (4, 5, 6)):
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


def step(program: List[str], pointer: int = 0) -> Tuple[List[str], int]:
    """
    Execute the instruction at the given position in the program. Continue
    calling step until reaching opcode 99 and halt the program, returning the
    final state of memory.
    """
    opcode, *modes = parse_opvalue(program[pointer])
    if opcode == 99:  # halt
        return program, pointer
    else:
        op = operations[opcode]
        args = parse_parameters(program, pointer, modes)
        program, pointer = op(program, pointer, *args)
        return step(program, pointer)


def main(inputfile: str) -> Tuple[List[str], int]:
    """
    Part 1: After providing 1 to the only input instruction and passing all the
    tests, what diagnostic code does the program produce?
    Part 2: What is the diagnostic code for system ID 5?
    """
    program = parse_input(inputfile)
    memory, pointer = step(program)
    return memory, pointer


if __name__ == '__main__':
    main('input_day05.txt')
