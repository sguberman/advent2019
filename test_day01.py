import day01


def test_fuel_required():
    assert day01.fuel_required(12) == 2
    assert day01.fuel_required(14) == 2
    assert day01.fuel_required(1969) == 654
    assert day01.fuel_required(100756) == 33583


def test_fuel_required_for_fuel():
    assert day01.fuel_required(14, include_fuel_mass=True) == 2
    assert day01.fuel_required(1969, include_fuel_mass=True) == 966
    assert day01.fuel_required(100756, include_fuel_mass=True) == 50346


def test_part1():
    assert day01.part1('input_day01.txt') == 3317659


def test_part2():
    assert day01.part2('input_day01.txt') == 4973616
