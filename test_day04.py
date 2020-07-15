import day04


def test_get_digits():
    assert day04.get_digits(223450) == [2, 2, 3, 4, 5, 0]


def test_has_double_digits():
    assert day04.has_double_digits(111111) is True
    assert day04.has_double_digits(223450) is True
    assert day04.has_double_digits(123789) is False


def test_never_decreases():
    assert day04.never_decreases(111111) is True
    assert day04.never_decreases(223450) is False
    assert day04.never_decreases(123789) is True


def test_meets_criteria():
    criteria = [day04.has_double_digits, day04.never_decreases]
    assert day04.meets_criteria(111111, criteria) is True
    assert day04.meets_criteria(223450, criteria) is False
    assert day04.meets_criteria(123789, criteria) is False


def test_part1():
    assert day04.part1('145852-616942') == 1767
