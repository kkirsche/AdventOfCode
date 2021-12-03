# Day 2: Dive!
from dataclasses import dataclass
from enum import Enum, unique
from unittest import TestCase, main


@dataclass
class Coordinates:
    depth: int = 0
    position: int = 0
    aim: int = 0
    use_aim: bool = False

    @property
    def location(self) -> int:
        return self.depth * self.position


@unique
class Direction(str, Enum):
    UP = "up"
    DOWN = "down"
    FORWARD = "forward"

    def __str__(self) -> str:
        return self.value


class Instruction:
    direction: Direction
    distance: int

    def __init__(self, instruction: str) -> None:
        (direction, distance) = instruction.split(" ")
        self.direction = Direction(direction)
        self.distance = int(distance)


@dataclass
class Submarine:
    use_aim: bool = False
    depth: int = 0
    position: int = 0
    aim: int = 0

    def deploy(self, route: list[Instruction]) -> Coordinates:
        for instruction in route:
            self.move(instruction)
        return self.coordinates

    @property
    def coordinates(self) -> Coordinates:
        return Coordinates(self.depth, self.position, self.aim, self.use_aim)

    def move(self, instruction: Instruction) -> None:
        if instruction.direction == Direction.UP:
            self.rise(instruction.distance)
        if instruction.direction == Direction.DOWN:
            self.dive(instruction.distance)
        if instruction.direction == Direction.FORWARD:
            self.forward(instruction.distance)

    def forward(self, distance: int = 0) -> None:
        self.position += distance
        if self.use_aim:
            self.depth += self.aim * distance

    def dive(self, depth: int = 0) -> None:
        if self.use_aim:
            self.aim += depth
        else:
            self.depth += depth

    def rise(self, depth: int = 0) -> None:
        if self.use_aim:
            self.aim -= depth
        else:
            self.depth -= depth

    def location(self) -> int:
        return self.depth * self.position


class TestImplementation(TestCase):
    def test_example_part1(self) -> None:
        content = "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2"
        instructions = [Instruction(line) for line in content.splitlines()]
        submarine = Submarine()
        coordinates = submarine.deploy(route=instructions)
        assert coordinates.location == Coordinates(depth=15, position=10).location

    def test_example_part2(self) -> None:
        content = "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2"
        instructions = [Instruction(line) for line in content.splitlines()]
        submarine = Submarine(use_aim=True)
        coordinates = submarine.deploy(route=instructions)
        assert (
            coordinates.location
            == Coordinates(depth=60, position=15, aim=10, use_aim=True).location
        )

    def test_part1(self) -> None:
        instructions = []
        submarine = Submarine(use_aim=False)
        with open("inputs/day2.txt", mode="r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    instructions.append(Instruction(line))
        coordinates = submarine.deploy(route=instructions)
        assert coordinates.location == Coordinates(depth=741, position=1998).location

    def test_part2(self) -> None:
        instructions = []
        submarine = Submarine(use_aim=True)
        with open("inputs/day2.txt", mode="r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    instructions.append(Instruction(line))
        coordinates = submarine.deploy(route=instructions)
        assert (
            coordinates.location
            == Coordinates(depth=642_047, position=1998, aim=741, use_aim=True).location
        )


if __name__ == "__main__":
    main()
