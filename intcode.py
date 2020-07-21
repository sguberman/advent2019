from __future__ import annotations
from collections import deque
from itertools import zip_longest
from typing import Callable, Deque, Dict, List, Optional, Tuple


Memory = List[int]


class Computer:

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

    def __init__(self, memory: Memory) -> None:
        '''
        Initialize a new Computer.
        '''
        self.memory: Memory = memory
        self.pointer: int = 0
        self.set_inputs()
        self.outputs: List[int] = []
        self.log_output: bool = False

        self.operations: Dict[int, Callable] = {  # opcode -> function
            1: self.add,
            2: self.mul,
            3: self.inp,
            4: self.out,
            5: self.jit,
            6: self.jif,
            7: self.clt,
            8: self.ceq,
        }

    def set_inputs(self, inputs: Optional[List[int]] = None) -> None:
        if not inputs:
            inputs = []
        self.inputs: Deque[int] = deque(inputs)

    @classmethod
    def from_file(cls, program_filename: str) -> Computer:
        '''
        Create a new Computer instance from a given program_filename.
        '''
        memory: Memory = [int(x)
                          for x in open(program_filename).read().split(',')]
        return cls(memory)

    def add(self, a: int, b: int, address: int) -> None:
        """
        Opcode: 1
        Add a and b, storing the result in the given address in memory.
        """
        self.memory[address] = a + b
        self.pointer += self.num_params[1] + 1

    def mul(self, a: int, b: int, address: int) -> None:
        """
        Opcode: 2
        Multiply a and b, storing the result in the given address in memory.
        """
        self.memory[address] = a * b
        self.pointer += self.num_params[2] + 1

    def inp(self, address: int) -> None:
        """
        Opcode: 3
        If program inputs are available, take one. Otherwise get input from
        the user. Store it at the given address in the memory.
        """
        if self.inputs:
            program_input = self.inputs.popleft()
            if self.log_output:
                print('PROGRAM INPUT: ', program_input)
        else:
            while True:
                user_input = input('Enter integer: ')
                try:
                    program_input = int(user_input)
                    break
                except ValueError as e:
                    print(e)
                    print('Invalid input, try again.')
        self.memory[address] = program_input
        self.pointer += self.num_params[3] + 1

    def out(self, value: int) -> int:
        """
        Opcode: 4
        Print the provided value, if log_outputs is enabled. Append the value
        to program outputs.
        """
        if self.log_output:
            print('PROGRAM OUTPUT: ', value)
        self.outputs.append(value)
        self.pointer += self.num_params[4] + 1
        return value

    def jit(self, a: int, b: int) -> None:
        """
        Opcode: 5
        If a is non-zero, set the pointer to b.
        """
        if a != 0:
            self.pointer = b
        else:
            self.pointer += self.num_params[5] + 1

    def jif(self, a: int, b: int) -> None:
        """
        Opcode: 6
        If a is zero, set the pointer to b.
        """
        if a == 0:
            self.pointer = b
        else:
            self.pointer += self.num_params[6] + 1

    def clt(self, a: int, b: int, address: int) -> None:
        """
        Opcode: 7
        If a is less than b, store 1 at the address in memory.
        Otherwise store 0.
        """
        if a < b:
            self.memory[address] = 1
        else:
            self.memory[address] = 0
        self.pointer += self.num_params[7] + 1

    def ceq(self, a: int, b: int, address: int) -> None:
        """
        Opcode: 8
        If a is equal to b, store 1 at the address in memory.
        Otherwise store 0.
        """
        if a == b:
            self.memory[address] = 1
        else:
            self.memory[address] = 0
        self.pointer += self.num_params[8] + 1

    @classmethod
    def parse_opvalue(cls, opvalue: int) -> Tuple[int, ...]:
        """
        Parse the first value of an instruction, returning a tuple of the
        opcode and parameter modes as ints.
        """
        opcode = int(str(opvalue)[-2:])
        modes: List[int] = [
            int(x)
            for x, _ in zip_longest(str(opvalue)[-3::-1],
                                    range(cls.num_params[opcode]),
                                    fillvalue=0)]
        # Destination address is always immediate for ops that store a value.
        if modes and (opcode not in (4, 5, 6)):
            modes[-1] = 1
        return opcode, *modes

    def parse_parameters(self, modes: List[int]) -> List[int]:
        """
        Parse the parameters for an instruction beginning at pointer
        using the provided parameter modes.
        """
        parameters = []
        for mode, value in zip(modes, self.memory[self.pointer + 1:]):
            if mode == 0:  # position mode
                parameter = self.memory[value]
            elif mode == 1:  # immediate mode
                parameter = value
            parameters.append(parameter)
        return parameters

    def run(
            self,
            with_inputs: Optional[List[int]] = None,
            stop_at_first_output: bool = False,
            log_output: bool = False) -> List[int]:
        """
        Run the program in memory, starting from address 0, until reaching
        a halt opcode. Return a list of any program outputs.
        """
        if with_inputs:
            self.set_inputs(with_inputs)
        self.log_output = log_output
        while True:
            opcode, *modes = self.parse_opvalue(self.memory[self.pointer])
            if opcode == 99:  # halt
                return self.outputs
            else:
                op = self.operations[opcode]
                args = self.parse_parameters(modes)
                output = op(*args)
                if stop_at_first_output and output:
                    return self.outputs


if __name__ == '__main__':
    c = Computer.from_file('input_day05.txt')
    output = c.run(with_inputs=[5], stop_at_first_output=True, log_output=True)
    print(output)
