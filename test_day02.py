import day02


def test_step():
    assert day02.step([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert day02.step([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert day02.step([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert day02.step([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [
        30, 1, 1, 4, 2, 5, 6, 0, 99]


def test_part1():
    assert day02.part1('input_day02.txt') == 3516593


def test_determine_inputs():
    program = day02.parse_input('input_day02.txt')
    assert day02.determine_inputs(program, 3516593) == (12, 2)


def test_part2():
    assert day02.part2('input_day02.txt') == 7749
