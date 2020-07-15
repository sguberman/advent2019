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


def part1(inputstring: str) -> int:
    """
    How many different passwords within the range given in your puzzle input
    meet these criteria?
    """
    lower, upper = map(int, inputstring.split('-'))
    criteria = [has_double_digits, never_decreases]
    return sum(meets_criteria(pw, criteria) for pw in range(lower, upper + 1))
