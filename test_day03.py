import day03


def test_parse_line():
    line = 'R75,D30,R83,U83'
    expected = day03.wirepoints([('R', 75), ('D', 30), ('R', 83), ('U', 83)])
    assert day03.parse_line(line) == expected


def test_manhattan_distance():
    assert day03.manhattan_distance((3, 3), (0, 0)) == 6
    assert day03.manhattan_distance((3, 3), (3, 3)) == 0
    assert day03.manhattan_distance((1, 1), (-1, -1)) == 4
    assert day03.manhattan_distance((-1, -1), (1, 1)) == 4


def test_intersections():
    line_a = 'R8,U5,L5,D3'
    line_b = 'U7,R6,D4,L4'
    wire_a = day03.parse_line(line_a)
    wire_b = day03.parse_line(line_b)
    intersections = day03.find_intersections([wire_a, wire_b])
    assert (3, 3) in intersections
    assert (6, 5) in intersections
    assert day03.closest_to_port(intersections) == (6, (3, 3))


def test_part1():
    assert day03.part1('input_day03.txt') == 529


def test_steps_to():
    line_a = 'R8,U5,L5,D3'
    line_b = 'U7,R6,D4,L4'
    wire_a = day03.parse_line(line_a)
    wire_b = day03.parse_line(line_b)
    assert day03.steps_to((3, 3), wire_a) == 20
    assert day03.steps_to((3, 3), wire_b) == 20


def test_shortest_path():
    line_a = 'R8,U5,L5,D3'
    line_b = 'U7,R6,D4,L4'
    wire_a = day03.parse_line(line_a)
    wire_b = day03.parse_line(line_b)
    assert day03.shortest_path([wire_a, wire_b]) == (30, (6, 5))


def test_part2():
    assert day03.part2('input_day03.txt') == 20386
