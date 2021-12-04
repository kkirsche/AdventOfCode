# Day 4: Giant Squid
from typing import Optional
from unittest import TestCase

from adventofcode.data import load_puzzle


class AnnouncedNumberStrategy:
    announcement: str  # the order before it's been parsed
    _order: Optional[list[str]] = None

    def __init__(self, announcement: str) -> None:
        self.announcement = announcement

    @property
    def order(self) -> list[str]:
        if self._order is None:
            self._order = [x for x in self.announcement.split(",")]
        return self._order


class BingoBoard:
    grid: list[list[str]]
    _rows: Optional[list[str]] = None
    _columns: Optional[list[str]] = None
    _join_row_char: str = " "
    _join_column_char: str = "\n"

    def __str__(self) -> str:
        """__str__ returns the grid as a string.

        This returns the list of lists as a string where the
        Returns:
            str: [description]
        """
        return self._join_column_char.join(
            [self._join_row_char.join(x) for x in self.grid]
        )

    def __init__(self, rows: list[str]) -> None:
        self._rows = rows
        self.grid = []
        for row in rows:
            columns = row.split(" ")
            self.grid.append(columns)

    @property
    def rows(self) -> list[str]:
        if self._rows is None:
            self._rows = [self._join_row_char.join(row) for row in self.grid]
        return self._rows

    @property
    def columns(self) -> list[str]:
        if self._columns is None:
            self._columns = []
            row_length = len(self.grid[0])
            self._columns = []
            for row in self.grid:
                column = [row[i] for i in range(row_length)]
                self._columns.append(self._join_column_char.join(column))
        return self._columns


class BingoPuzzle:
    puzzle_definition: str
    boards: list[BingoBoard]
    strategy: AnnouncedNumberStrategy

    def __init__(self, puzzle_definition: str) -> None:
        self.boards = []
        self.puzzle_definition = puzzle_definition
        self._parse_puzzle_definition()

    def _parse_puzzle_definition(self) -> None:
        puzzle_lines = self.puzzle_definition.split("\n")
        self.strategy = AnnouncedNumberStrategy(puzzle_lines.pop(0))
        puzzles = "\n".join(puzzle_lines).split("\n\n")
        for puzzle in puzzles:
            self.boards.append(BingoBoard(rows=puzzle.split("\n")))


class TestDay4Solution(TestCase):
    def test_example_pt1(self) -> None:
        challenge = load_puzzle(day=4, example=True, filter_none=False)
        puzzle = BingoPuzzle("\n".join(challenge))
        assert len(puzzle.boards) == 3

    # def test_pt1(self) -> None:
    #     diagnostic_report = self.load_report(example=False)
    #     interpreter = DiagnosticReportInterpretor(report=diagnostic_report)
    #     assert interpreter.power_consumption == 1_307_354
