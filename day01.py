from typing import Iterable


def fuel_required(mass: int, include_fuel_mass: bool = False) -> int:
    fuel_for_mass = (mass // 3) - 2
    if fuel_for_mass < 0:
        return 0
    elif include_fuel_mass:
        return fuel_for_mass + fuel_required(fuel_for_mass, True)
    else:
        return fuel_for_mass


def total_fuel(masses: Iterable[int], include_fuel_mass: bool = False) -> int:
    return sum(fuel_required(mass, include_fuel_mass) for mass in masses)


def parse_input(inputfile: str) -> Iterable[int]:
    for line in open(inputfile):
        yield int(line)


def part1(inputfile: str) -> int:
    return total_fuel(parse_input(inputfile))


def part2(inputfile: str) -> int:
    return total_fuel(parse_input(inputfile), include_fuel_mass=True)


if __name__ == '__main__':
    print(part1('input_day01.txt'))
    print(part2('input_day01.txt'))
