"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730236204"


class Simpy:
    """Simpy class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Part 0."""
        self.values = values
    
    def __str__(self) -> str:
        """Part 1."""
        return f"Simpy({self.values})"
    
    def __repr__(self) -> str:
        """Part 1."""
        return f"Simpy({self.values})"
    
    def fill(self, x: float, y: int) -> None:
        """Part 2."""
        self.values = []
        i = 0
        while i < y:
            self.values.append(float(x))
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Part 3."""
        self.values = []
        x = start
        if start > stop:
            while x > stop:
                if x == stop:
                    self.values.append(x)
                if x > stop:
                    self.values.append(x)
                x += step
        else:
            while x < stop:
                if x == stop:
                    self.values.append(x)
                if x < stop:
                    self.values.append(x)
                x += step

    def sum(self) -> float:
        """Part 4."""
        sum_val: float
        sum_val = sum(self.values)
        return sum_val
        
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Part 5."""
        add_res = []
        if isinstance(rhs, float):
            for item in self.values:
                add_sum = item + rhs
                add_res.append(add_sum)
        else:
            for i in range(0, len(self.values)):
                add_res.append(self.values[i] + rhs.values[i])
        return Simpy(add_res)
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Part 6."""
        add_res = []
        if isinstance(rhs, float):
            for item in self.values:
                add_sum = item ** rhs
                add_res.append(add_sum)
        else:
            for i in range(0, len(self.values)):
                add_res.append(self.values[i] ** rhs.values[i])
        return Simpy(add_res)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Part 7."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for i in range(0, len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Part 8."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            for i in range(0, len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Parts 9 and 10."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: list[float] = []
            for i in range(len(self.values)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)