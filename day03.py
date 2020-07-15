from typing import List, Set, Tuple


Gridpoint = Tuple[int, int]
Command = Tuple[str, int]
Wirepath = List[Command]
Wire = List[Gridpoint]


def parse_line(line: str) -> Wirepath:
    """
    Parse a line from the inputfile into a list of (str, int) tuples.
    """
    wirepath = []
    commands = line.split(',')
    for command in commands:
        direction = command[0]
        distance = int(command[1:])
        wirepath.append((direction, distance))
    return wirepath


def parse_input(inputfile: str) -> List[Wirepath]:
    """
    Read the inputfile, parsing each line into a list of (str, int) tuples.
    Return a list of the lists.
    """
    wirepaths = []
    for line in open(inputfile):
        wirepath = parse_line(line)
        wirepaths.append(wirepath)
    return wirepaths


def wirepoints(wirepath: Wirepath) -> Wire:
    """
    Given a path for a wire (from parse_line()), return a list of points on
    the grid that it passes through.
    """
    points = []
    x, y = 0, 0
    for direction, distance in wirepath:
        if direction == 'U':
            for _ in range(distance):
                y += 1
                points.append((x, y))
        elif direction == 'D':
            for _ in range(distance):
                y -= 1
                points.append((x, y))
        elif direction == 'R':
            for _ in range(distance):
                x += 1
                points.append((x, y))
        elif direction == 'L':
            for _ in range(distance):
                x -= 1
                points.append((x, y))
        else:
            raise ValueError
    return points


def manhattan_distance(a: Gridpoint, b: Gridpoint) -> int:
    """
    Return the manhattan distance between two points on the grid.
    """
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)


def find_intersections(wires: List[Wire]) -> Set[Gridpoint]:
    """
    Find the set of grid points where the wires cross.
    """
    pointsets = [set(wire) for wire in wires]
    return set.intersection(*pointsets)


def closest_to_port(intersections: Set[Gridpoint]) -> Tuple[int, Gridpoint]:
    """
    Find the intersection closest to (0, 0) based on manhattan distance.
    """
    return min((manhattan_distance(p, (0, 0)), p) for p in intersections)


def part1(inputfile: str) -> int:
    """
    What is the manhattan distance from the central port to the closest
    intersection?
    """
    wires = [wirepoints(w) for w in parse_input('input_day03.txt')]
    distance, _ = closest_to_port(find_intersections(wires))
    return distance
