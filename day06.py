from typing import Dict, Iterable, List, Optional, Union


ParentDict = Dict[str, str]


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


def build_map(inputfile: str) -> ParentDict:
    '''
    For each orbit in the inputfile, add the relationship to the
    child->parent dictionary. Return the dictionary.
    '''
    parent_of: ParentDict = {}
    for parent, child in parse_input(inputfile):
        parent_of[child] = parent
    return parent_of


def count_orbits(
        parent_of: ParentDict,
        child: str,
        root: Optional[str] = 'COM') -> int:
    '''
    Count the number of direct and indirect orbits for a given object in space.
    '''
    if child == root:
        return 0
    else:
        return 1 + count_orbits(parent_of, parent_of[child], root)


def orbit_checksum(inputfile: str) -> int:
    '''
    Count the total number of direct and indirect orbits in a given inputfile.
    '''
    parent_of = build_map(inputfile)
    return sum(count_orbits(parent_of, child) for child in parent_of)


def part1(inputfile: str) -> int:
    '''
    What is the total number of direct and indirect orbits in your map data?
    '''
    return orbit_checksum(inputfile)


def path_to_root(
        parent_of: ParentDict,
        child: str,
        root: Optional[str] = 'COM') -> List[str]:
    '''
    Trace the path from the child node back to the root of the parent_of dict.
    Return as a list of str.
    '''
    if child == root:
        return []
    else:
        parent = parent_of[child]
        return [parent] + path_to_root(parent_of, parent, root)


def common_node(
        origin_path: List[str],
        destination_path: List[str]) -> Union[str, None]:
    '''
    Return the first node in origin_path that is also in destination_path.
    Otherwise return None.
    '''
    for node in origin_path:
        if node in destination_path:
            return node
    return None


def count_orbital_transfers(
        parent_of: ParentDict,
        origin: str,
        destination: str) -> int:
    '''
    Count the minimum number of orbital transfers needed to transfer the origin
    object to the same orbit as the destination object.
    '''
    origin_path = path_to_root(parent_of, origin)
    destination_path = path_to_root(parent_of, destination)
    common = common_node(origin_path, destination_path)
    origin_to_common = count_orbits(parent_of, origin, common)
    destination_to_common = count_orbits(parent_of, destination, common)
    return origin_to_common + destination_to_common - 2


def part2(inputfile: str) -> int:
    '''
    What is the minimum number of orbital transfers required to move the from
    the object YOU are orbiting to the object SAN is orbiting?
    '''
    return count_orbital_transfers(build_map(inputfile), 'YOU', 'SAN')


if __name__ == '__main__':
    print(part1('input_day06.txt'))
    print(part2('input_day06.txt'))
