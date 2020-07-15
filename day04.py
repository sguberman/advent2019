from itertools import zip_longest
from typing import Callable, List


def get_digits(password: int) -> List[int]:
    """
    Given an int, return a list of int digits.
    """
    return [int(x) for x in str(password)]


def has_double_digits(password: int) -> bool:
    """
    Return True if the password has at least two consecutive repeating digits,
    otherwise return False.
    """
    digits = get_digits(password)
    return any(a == b for a, b in zip(digits, digits[1:]))


def never_decreases(password: int) -> bool:
    """
    Return True if the digits in the password never decrease from left to
    right, otherwise return False.
    """
    digits = get_digits(password)
    return all(b >= a for a, b in zip(digits, digits[1:]))


def meets_criteria(password: int, criteria: List[Callable]) -> bool:
    """
    Return True if the password meets all of the criteria provided.
    """
    return all(criterion(password) for criterion in criteria)


def count_valid_passwords(
        lower: int,
        upper: int,
        criteria: List[Callable]) -> int:
    """
    Count the number of passwords in range lower-upper (inclusive) that
    meet the given criteria.
    """
    return sum(meets_criteria(pw, criteria) for pw in range(lower, upper + 1))


def part1(inputstring: str) -> int:
    """
    How many different passwords within the range given in your puzzle input
    meet these criteria?
    """
    lower, upper = map(int, inputstring.split('-'))
    criteria = [has_double_digits, never_decreases]
    return count_valid_passwords(lower, upper, criteria)


def has_standalone_double_digits(password: int) -> bool:
    """
    Return True if a password has two adjacent matching digits that are not
    part of a larger group of matching digits, otherwise return False.
    """
    digits = get_digits(password)
    a, b, c = digits[:3]
    if a == b != c:  # check first two digits
        return True
    else:
        quads = zip_longest(digits, digits[1:], digits[2:], digits[3:])
        return any(a != b == c != d for a, b, c, d in quads)


def part2(inputstring: str) -> int:
    """
    How many different passwords within the range given in your puzzle input
    meet all the criteria?
    """
    lower, upper = map(int, inputstring.split('-'))
    criteria = [has_standalone_double_digits, never_decreases]
    return count_valid_passwords(lower, upper, criteria)


if __name__ == '__main__':
    inputstring = '145852-616942'
    print(part1(inputstring))
    print(part2(inputstring))
