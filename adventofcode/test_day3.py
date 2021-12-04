# Day 3: Binary Diagnostics
from collections import Counter
from dataclasses import dataclass, field
from typing import Optional
from unittest import TestCase

from adventofcode.data import load_puzzle


@dataclass
class Locations:
    zeros: set[int] = field(default_factory=set)
    ones: set[int] = field(default_factory=set)

    @property
    def most_common(self) -> str:
        zeros = len(self.zeros)
        ones = len(self.ones)
        if zeros > ones:
            return "0"
        else:
            return "1"

    @property
    def least_common(self) -> str:
        zeros = len(self.zeros)
        ones = len(self.ones)
        if zeros > ones:
            return "1"
        else:
            return "0"

    def update(self, value: str, location: int) -> None:
        if value == "0":
            self.zeros.add(location)
        elif value == "1":
            self.ones.add(location)
        else:
            raise ValueError(f"Invalid value: {value}")

    def as_ignore_filter(self, value: str) -> set[int]:
        if value == "0":
            return self.ones
        elif value == "1":
            return self.zeros
        else:
            raise ValueError(f"Invalid value: {value}")


@dataclass
class DiagnosticReportInterpretor:
    report: list[str]
    _gamma_rate: str = ""
    _epsilon_rate: str = ""
    _oxygen_generator_rating: str = ""
    _co2_scrubber_rating: str = ""

    @property
    def gamma_rate(self) -> int:
        if not self._gamma_rate:
            self.generate_gamma_and_epsilon_rate()
        return int(self._gamma_rate, 2)

    @property
    def epsilon_rate(self) -> int:
        if not self._epsilon_rate:
            self.generate_gamma_and_epsilon_rate()
        return int(self._epsilon_rate, 2)

    @property
    def oxygen_generator_rating(self) -> int:
        if not self._oxygen_generator_rating:
            self.generate_oxygen_generator_rating()
        return int(self._oxygen_generator_rating, 2)

    @property
    def co2_scrubber_rating(self) -> int:
        if not self._co2_scrubber_rating:
            self.generate_co2_scrubber_rating()
        return int(self._co2_scrubber_rating, 2)

    @property
    def power_consumption(self) -> int:
        return self.gamma_rate * self.epsilon_rate

    @property
    def life_support_rating(self) -> int:
        return self.oxygen_generator_rating * self.co2_scrubber_rating

    def generate_gamma_and_epsilon_rate(self, bit: int = 0) -> str:
        counter = Counter({"0": 0, "1": 0})
        for number in self.report:
            if bit >= len(number):
                return self._gamma_rate
            counter.update(number[bit])
        commonality = counter.most_common()
        most_common = commonality[0][0]
        least_common = commonality[-1][0]
        self._gamma_rate += most_common
        self._epsilon_rate += least_common
        return self.generate_gamma_and_epsilon_rate(bit=bit + 1)

    def generate_oxygen_generator_rating(
        self, bit: int = 0, report: Optional[list[str]] = None
    ) -> str:
        if report is None:
            report = self.report
        if len(report) == 0:
            return self._oxygen_generator_rating
        locations = Locations()
        for idx, number in enumerate(report):
            try:
                locations.update(value=number[bit], location=idx)
            except IndexError:
                return self._oxygen_generator_rating
        self._oxygen_generator_rating += locations.most_common
        next_report = [
            number
            for idx, number in enumerate(report)
            if idx not in locations.as_ignore_filter(locations.most_common)
        ]
        return self.generate_oxygen_generator_rating(bit=bit + 1, report=next_report)

    def generate_co2_scrubber_rating(
        self, bit: int = 0, report: Optional[list[str]] = None
    ) -> str:
        if report is None:
            report = self.report
        if len(report) == 1:
            self._co2_scrubber_rating = report.pop()
            return self._co2_scrubber_rating

        locations = Locations()
        for idx, number in enumerate(report):
            locations.update(value=number[bit], location=idx)

        next_report = [
            number
            for idx, number in enumerate(report)
            if idx not in locations.as_ignore_filter(locations.least_common)
        ]
        return self.generate_co2_scrubber_rating(bit=bit + 1, report=next_report)


class TestDay3Solution(TestCase):
    def load_report(self, example: bool = False) -> list[str]:
        return load_puzzle(3, example)

    def test_example_pt1(self) -> None:
        diagnostic_report = self.load_report(example=True)
        interpreter = DiagnosticReportInterpretor(report=diagnostic_report)
        assert interpreter.gamma_rate == 22
        assert interpreter._gamma_rate == "10110"
        assert interpreter.epsilon_rate == 9
        assert interpreter._epsilon_rate == "01001"
        assert interpreter.power_consumption == 198

    def test_example_pt2(self) -> None:
        diagnostic_report = self.load_report(example=True)
        interpreter = DiagnosticReportInterpretor(report=diagnostic_report)
        assert interpreter.oxygen_generator_rating == 23
        assert interpreter._oxygen_generator_rating == "10111"
        assert interpreter.co2_scrubber_rating == 10
        assert interpreter._co2_scrubber_rating == "01010"
        assert interpreter.life_support_rating == 230

    def test_pt1(self) -> None:
        diagnostic_report = self.load_report(example=False)
        interpreter = DiagnosticReportInterpretor(report=diagnostic_report)
        assert interpreter.power_consumption == 1_307_354

    def test_pt2(self) -> None:
        diagnostic_report = self.load_report(example=False)
        interpreter = DiagnosticReportInterpretor(report=diagnostic_report)
        interpreter.life_support_rating
        assert interpreter.life_support_rating == 482_500
