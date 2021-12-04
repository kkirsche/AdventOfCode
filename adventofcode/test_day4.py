# Day 4: Giant Squid
from abc import ABC, abstractmethod
from typing import Optional, Type
from unittest import TestCase

from adventofcode.data import load_puzzle


class Coordinate:
    x: int
    y: int

    def __init__(self, x: int, y: int, value: int) -> None:
        self.x = x
        self.y = y
        self.value = value

    def as_tuple(self) -> tuple[int, int]:
        return self.x, self.y

    def as_dict(self) -> dict[str, int]:
        return {"x": self.x, "y": self.y}

    def __str__(self) -> str:
        return f"({self.x+1}, {self.y+1}) - {self.value}"

    def __repr__(self) -> str:
        return self.__str__()


class BingoBoard:
    id: int
    grid: list[list[int]]
    _hit_spaces: list[Coordinate]

    def __init__(self, puzzle: str, id: int) -> None:
        self.id = id
        self.grid = [
            [int(column) for column in row.split(" ") if column != ""]
            for row in puzzle.split("\n")
            if row != ""
        ]
        self._hit_spaces = []

    def play(self, value: int) -> None:
        coordinate = self.locate(value=value)
        if coordinate is not None:
            self._hit_spaces.append(coordinate)

    @property
    def rows(self) -> list[set[int]]:
        return [set(row) for row in self.grid]

    @property
    def columns(self) -> list[set[int]]:
        return [set(column) for column in zip(*self.grid)]

    @property
    def diagnols(self) -> list[set[int]]:
        edge_length = len(self.grid)
        diagnols = []
        for direction in range(2):
            if direction == 0:
                diagnol = {
                    self.grid[location][location] for location in range(edge_length)
                }
                diagnols.append(diagnol)
            elif direction == 1:
                diagnol = set()
                for location in range(edge_length):
                    inverted = edge_length - 1 - location
                    diagnol.add(self.grid[inverted][inverted])
                diagnols.append(diagnol)
        return diagnols

    def check_bingo(self) -> bool:
        hits = {hit.value for hit in self._hit_spaces}
        hit_count = len(hits)
        if hit_count < 5:
            return False
        return any(
            len(v.intersection(hits)) == 5
            for v in self.rows + self.columns + self.diagnols
        )

    @property
    def unmarked_sum(self) -> int:
        hits = {hit.value for hit in self._hit_spaces}
        score = 0
        for row in self.grid:
            for value in row:
                if value not in hits:
                    score += value
        return score

    @property
    def score(self) -> int:
        return self.unmarked_sum * self.retrieve(self._hit_spaces[-1])

    def __str__(self) -> str:
        """__str__ returns the grid as a string.

        This returns the list of lists as a string where the
        Returns:
            str: [description]
        """
        return "\n".join([" ".join(str(x)) for x in self.grid])

    def locate(self, value: int) -> Optional[Coordinate]:
        for idx, row in enumerate(self.grid):
            if value in row:
                return Coordinate(x=row.index(value), y=idx, value=value)
        return None

    def retrieve(self, coordinate: Coordinate) -> int:
        return self.grid[coordinate.y][coordinate.x]


class Strategy(ABC):
    announcement: str  # the order before it's been parsed
    _order: Optional[list[int]] = None

    def __init__(self, announcement: str) -> None:
        self.announcement = announcement

    @property
    def order(self) -> list[int]:
        if self._order is None:
            self._order = [int(x) for x in self.announcement.split(",")]
        return self._order

    @abstractmethod
    def play_boards(self, boards: list[BingoBoard]) -> tuple[BingoBoard, int]:
        pass


class FirstBoard(Strategy):
    def play_boards(self, boards: list[BingoBoard]) -> tuple[BingoBoard, int]:
        for value in self.order:
            for board in boards:
                board.play(value)
                if board.check_bingo():
                    print(f"Bingo for {board.id} with {value}")
                    return board, value
        raise ValueError("No winning board found")


class FinalBoard(Strategy):
    def play_boards(self, boards: list[BingoBoard]) -> tuple[BingoBoard, int]:
        excluded = set()
        for value in self.order:
            for board in boards:
                if board.id in excluded:
                    continue
                board.play(value)
                if board.check_bingo():
                    excluded.add(board.id)
                    print(f"Bingo for {board.id} with {value}")
                    if len(excluded) == len(boards):
                        return board, value
        raise ValueError("No winning board found")


class BingoPuzzle:
    puzzle_definition: str
    boards: list[BingoBoard]
    strategy_type: Type[Strategy]
    strategy: Strategy
    winner: Optional[BingoBoard] = None
    winning_number: Optional[int] = None

    def __init__(self, puzzle_definition: str, strategy_type: Type[Strategy]) -> None:
        self.boards = []
        self.puzzle_definition = puzzle_definition
        self.strategy_type = strategy_type
        self._parse_puzzle_definition()

    def _parse_puzzle_definition(self) -> None:
        puzzle_lines = self.puzzle_definition.split("\n")
        self.strategy = self.strategy_type(puzzle_lines.pop(0))
        puzzles = "\n".join(puzzle_lines).split("\n\n")
        for idx, puzzle in enumerate(puzzles):
            self.boards.append(BingoBoard(puzzle=puzzle, id=idx + 1))

    def play(self) -> None:
        winner, winning_number = self.strategy.play_boards(self.boards)
        self.winner = winner
        self.winning_number = winning_number


class TestDay4Solution(TestCase):
    def test_example_structure(self) -> None:
        challenge = load_puzzle(day=4, example=True, filter_none=False)
        puzzle = BingoPuzzle(
            puzzle_definition="\n".join(challenge), strategy_type=FirstBoard
        )
        # Ensure we parsed the puzzle correctly
        # start with the number of puzzles and the size of them
        assert len(puzzle.boards) == 3
        assert puzzle.boards[0].rows[0] == {22, 13, 17, 11, 0}
        assert puzzle.boards[0].columns[0] == {22, 8, 21, 6, 1}
        assert puzzle.boards[0].diagnols[0] == {22, 2, 14, 18, 19}

    def test_example_pt1(self) -> None:
        challenge = load_puzzle(day=4, example=True, filter_none=False)
        puzzle = BingoPuzzle(
            puzzle_definition="\n".join(challenge), strategy_type=FirstBoard
        )
        puzzle.play()
        # verify the winning number is correct, in both locations
        assert puzzle.winning_number == 24
        assert puzzle.winner is not None
        assert puzzle.winner.retrieve(puzzle.winner._hit_spaces[-1]) == 24
        assert puzzle.winner.unmarked_sum == 188
        assert puzzle.winner.score == 4_512
        assert puzzle.winner.id == 3

    def test_example_pt2(self) -> None:
        challenge = load_puzzle(day=4, example=True, filter_none=False)
        puzzle = BingoPuzzle(
            puzzle_definition="\n".join(challenge), strategy_type=FinalBoard
        )
        puzzle.play()
        # verify the winning number is correct, in both locations
        assert puzzle.winning_number == 13
        assert puzzle.winner is not None
        assert puzzle.winner.retrieve(puzzle.winner._hit_spaces[-1]) == 13
        assert puzzle.winner.unmarked_sum == 148
        assert puzzle.winner.score == 1_924
        assert puzzle.winner.id == 2

    def test_pt1(self) -> None:
        challenge = load_puzzle(day=4, example=False, filter_none=False)
        puzzle = BingoPuzzle(
            puzzle_definition="\n".join(challenge), strategy_type=FirstBoard
        )
        # Ensure we parsed the puzzle correctly
        # start with the number of puzzles and the size of them
        puzzle.play()
        assert puzzle.winner is not None
        assert puzzle.winner.score == 55_770
        assert puzzle.winner.id == 76
        assert puzzle.winning_number == 78

    def test_pt2(self) -> None:
        challenge = load_puzzle(day=4, example=False, filter_none=False)
        puzzle = BingoPuzzle(
            puzzle_definition="\n".join(challenge), strategy_type=FinalBoard
        )
        # Ensure we parsed the puzzle correctly
        # start with the number of puzzles and the size of them
        puzzle.play()
        assert puzzle.winner is not None
        assert puzzle.winner.score == 2_980
        assert puzzle.winner.id == 45
        assert puzzle.winning_number == 10
