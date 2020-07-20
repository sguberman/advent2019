import day06


def test_parse_line():
    assert day06.parse_line('AAA)BBB') == ['AAA', 'BBB']
    assert day06.parse_line('COM)B') == ['COM', 'B']


def test_build_map():
    parent_of = day06.build_map('test_input_day06_part1.txt')
    assert parent_of['H'] == 'G'
    assert parent_of['L'] == 'K'


def test_count_orbits():
    parent_of = day06.build_map('test_input_day06_part1.txt')
    assert day06.count_orbits(parent_of, 'D') == 3
    assert day06.count_orbits(parent_of, 'L') == 7
    assert day06.count_orbits(parent_of, 'COM') == 0


def test_orbit_checksum():
    assert day06.orbit_checksum('test_input_day06_part1.txt') == 42


def test_part1():
    assert day06.part1('input_day06.txt') == 241064


def test_count_orbital_transfers():
    parent_of = day06.build_map('test_input_day06_part2.txt')
    assert day06.count_orbital_transfers(parent_of,
                                         origin='YOU',
                                         destination='SAN') == 4


def test_path_to_root():
    parent_of = day06.build_map('test_input_day06_part2.txt')
    assert day06.path_to_root(parent_of, 'YOU') == [
        'K', 'J', 'E', 'D', 'C', 'B', 'COM']
    assert day06.path_to_root(parent_of, 'SAN') == [
        'I', 'D', 'C', 'B', 'COM']


def test_common_node():
    parent_of = day06.build_map('test_input_day06_part2.txt')
    origin_path = day06.path_to_root(parent_of, 'YOU')
    destination_path = day06.path_to_root(parent_of, 'SAN')
    assert day06.common_node(origin_path, destination_path) == 'D'


def test_count_orbits_to_node():
    parent_of = day06.build_map('test_input_day06_part2.txt')
    assert day06.count_orbits(parent_of, 'YOU', 'D') == 4
    assert day06.count_orbits(parent_of, 'SAN', 'D') == 2


def test_part2():
    assert day06.part2('input_day06.txt') == 418
