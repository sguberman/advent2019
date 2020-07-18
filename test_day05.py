import day05


def test_parse_opvalue():
    assert day05.parse_opvalue('1002') == (2, 0, 1, 1)
    assert day05.parse_opvalue('1101') == (1, 1, 1, 1)
    assert day05.parse_opvalue('99') == (99,)
    assert day05.parse_opvalue('3') == (3, 1)
    assert day05.parse_opvalue('4') == (4, 0)
    assert day05.parse_opvalue('104') == (4, 1)


def test_parse_parameters():
    program = '1002,4,3,4,33'.split(',')
    pointer = 0
    _, *modes = day05.parse_opvalue(program[pointer])
    assert day05.parse_parameters(program, 0, modes) == [33, 3, 4]


def test_step():
    program = '1002,4,3,4,33'.split(',')
    assert day05.step(program, 0) == ('1002,4,3,4,99'.split(','), 4)
