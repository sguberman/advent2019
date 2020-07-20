import day06


def test_parse_line():
    assert day06.parse_line('AAA)BBB') == ['AAA', 'BBB']
    assert day06.parse_line('COM)B') == ['COM', 'B']


def test_build_map():
    parent_of, children_of = day06.build_map('test_input_day06.txt')
    assert parent_of['H'] == 'G'
    assert children_of['G'] == ['H']
    assert parent_of['L'] == 'K'
    assert set(children_of['D']) == set(['E', 'I'])


def test_count_orbits():
    parent_of, _ = day06.build_map('test_input_day06.txt')
    assert day06.count_orbits(parent_of, 'D') == 3
    assert day06.count_orbits(parent_of, 'L') == 7
    assert day06.count_orbits(parent_of, 'COM') == 0


def test_orbit_checksum():
    assert day06.orbit_checksum('test_input_day06.txt') == 42


def test_part1():
    assert day06.part1('input_day06.txt') == 241064
