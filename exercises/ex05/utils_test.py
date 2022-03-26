"""Function tests for EX 05."""

__author__ = "730236204"

from ex05.utils import only_evens, sub, concat


"""Tests for even number function."""


def test_only_evens_two_evens() -> None:
    """Testing for 2 even numbers in list."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_only_evens_one_even() -> None:
    """Testing for 1 even number in list."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_no_evens() -> None:
    """Testing for no even numbers in list."""
    assert only_evens([1, 3]) == []


"""Tests for sub function."""


def test_sub_first() -> None:
    """First test of sub for 1 and 3 index."""
    assert sub([1, 2, 3, 4], 1, 3) == [2, 3]


def test_sub_second() -> None:
    """Second test of sub for 2 and 4 index."""
    assert sub([1, 2, 3, 4, 5], 2, 4) == [3, 4]


def test_sub_third() -> None:
    """Third test of sub for 0 and 3 index."""
    assert sub([1, 2, 3, 4], 0, 3) == [1, 3]


"""Tests for concat function."""


def test_concat_first() -> None:
    """First test of concat putting two lists together."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_second() -> None:
    """Second test of concat putting one list and one empty list together."""
    assert concat([1, 2, 3], []) == [1, 2, 3]


def test_concat_third() -> None:
    """Third test of concat putting 2 empty lists together."""
    assert concat([], []) == []