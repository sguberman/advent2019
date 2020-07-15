from typing import List, Set, Tuple


Gridpoint = Tuple[int, int]
Command = Tuple[str, int]
Wirepath = List[Command]
Wire = List[Gridpoint]


def parse_line(line: str) -> Wire:
    """
    Parse a line from the inputfile into a list of (str, int) tuples.
    """
    wirepath = []
    commands = line.split(',')
    for command in commands:
        direction = command[0]
        distance = int(command[1:])
        wirepath.append((direction, distance))
    return wirepoints(wirepath)


def parse_input(inputfile: str) -> List[Wire]:
    """
    Read the inputfile, parsing each line into a list of (str, int) tuples.
    Return a list of the lists.
    """
    wires = []
    for line in open(inputfile):
        wire = parse_line(line)
        wires.append(wire)
    return wires


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
    wires = parse_input(inputfile)
    distance, _ = closest_to_port(find_intersections(wires))
    return distance


def steps_to(intersection: Gridpoint, wire: Wire) -> int:
    """
    Count the number of steps to an intersection point on a given wire.
    """
    return wire.index(intersection) + 1


def shortest_path(wires: List[Wire]) -> Tuple[int, Gridpoint]:
    """
    Find the intersection with the shortest combined number of steps along
    each wire.
    """
    intersections = find_intersections(wires)
    return min((sum(steps_to(p, w) for w in wires), p)
               for p in intersections)


def part2(inputfile: str) -> int:
    """
    What is the fewest combined steps the wires must take to reach an
    intersection?
    """
    distance, _ = shortest_path(parse_input(inputfile))
    return distance


if __name__ == '__main__':
    print(part1('input_day03.txt'))
    print(part2('input_day03.txt'))
