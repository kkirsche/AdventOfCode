from typing import Literal, Type

from pytest import mark


class Results:
    increased: int = 0
    decreased: int = 0


class Window:
    first: int
    second: int
    third: int

    def __init__(self, first: int = 0, second: int = 0, third: int = 0):
        self.first = first
        self.second = second
        self.third = third

    def sum(self) -> int:
        return self.first + self.second + self.third


class Solver:
    windowed: bool = False
    elevations: list[int]

    def __init__(self, elevations: list[int]) -> None:
        self.elevations = elevations


class Windowed(Solver):
    elevations: list[int]
    windowed: Literal[True] = True


class Singular(Solver):
    elevations: list[int]
    windowed: Literal[False] = False


def solve_not_windowed(elevations: list[int]) -> Results:
    """solve_not_windowed is the solution to part one of the AoC problem.

    Args:
        elevations (list[int]): The list of elevation numbers.

    Returns:
        Results: The number of times that the elevation increased and decreased.
    """
    results = Results()
    last = None
    for elevation in elevations:
        if last is None:
            last = elevation
            continue
        if elevation > last:
            results.increased += 1
        elif elevation < last:
            results.decreased += 1
        last = elevation
    return results


def solve_windowed(elevations: list[int]) -> Results:
    results = Results()
    last = None
    elevation_count = len(elevations)
    for idx, _ in enumerate(elevations):
        pop = idx - 1
        peek = idx + 1
        if pop < 0:
            continue
        if peek > (elevation_count - 1):
            continue
        window = Window(
            first=elevations[pop],
            second=elevations[idx],
            third=elevations[peek],
        )
        height = window.sum()
        if last is None:
            last = height
            continue
        if height > last:
            results.increased += 1
        elif height < last:
            results.decreased += 1
        last = height
    return results


def solve(solver: Solver) -> Results:
    if solver.windowed:
        return solve_windowed(solver.elevations)
    else:
        return solve_not_windowed(solver.elevations)


@mark.parametrize("kls, expected", [(Singular, 7), (Windowed, 5)])  # type: ignore
def test_example_part1(kls: Type[Solver], expected: int) -> None:
    challenge = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    solver = kls(elevations=challenge)
    results = solve(solver)
    assert results.increased == expected


@mark.parametrize("kls, expected", [(Singular, 1466), (Windowed, 1491)])  # type: ignore
def test_parts(kls: Type[Solver], expected: int) -> None:
    challenge = []
    with open("inputs/day1.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                challenge.append(int(line))
        solver = kls(elevations=challenge)
        results = solve(solver)
        assert results.increased == expected
