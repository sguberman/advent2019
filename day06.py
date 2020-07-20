from collections import defaultdict
from typing import Dict, Iterable, List, Tuple


def parse_line(line: str) -> List[str]:
    '''
    Parse one line of input, returning the parent and child as a tuple.
    '''
    return line.strip().split(')')


def parse_input(inputfile: str) -> Iterable[List[str]]:
    '''
    Generate one parsed line at a time from the inputfile.
    '''
    return (parse_line(line) for line in open(inputfile))


def build_map(inputfile: str) -> Tuple[Dict[str, str], Dict[str, List[str]]]:
    '''
    For each orbit in the inputfile, add the relationship to the
    child->parent and parent->children dictionaries. Return the dictionaries in
    a tuple.
    '''
    parent_of: Dict[str, str] = {}
    children_of: Dict[str, List[str]] = defaultdict(list)
    for parent, child in parse_input(inputfile):
        parent_of[child] = parent
        children_of[parent].append(child)
    return parent_of, children_of


def count_orbits(parent_of: Dict[str, str], child: str) -> int:
    '''
    Count the number of direct and indirect orbits for a given object in space.
    '''
    if child == 'COM':
        return 0
    else:
        return 1 + count_orbits(parent_of, parent_of[child])


def orbit_checksum(inputfile: str) -> int:
    '''
    Count the total number of direct and indirect orbits in a given inputfile.
    '''
    parent_of, _ = build_map(inputfile)
    return sum(count_orbits(parent_of, child) for child in parent_of)


def part1(inputfile: str) -> int:
    '''
    What is the total number of direct and indirect orbits in your map data?
    '''
    return orbit_checksum(inputfile)


if __name__ == '__main__':
    print(part1('input_day06.txt'))
