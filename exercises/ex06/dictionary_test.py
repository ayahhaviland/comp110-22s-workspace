"""Function tests for EX 06."""

__author__ = "730236204"

from ex06.dictionary import invert, favorite_color, count

"""Tests invert function."""


def test_invert1() -> None:
    """To test inversion of 1 dict."""
    assert invert({'orange': 'dog'}) == {'dog': 'orange'}


def test_invert2() -> None:
    """To test for key error."""
    assert invert({'ayah': 'haviland', 'iman': 'haviland'}) == KeyError


def test_invert3() -> None:
    """To test inversion of 3 dicts."""
    assert invert({'a': 'b', 'c': 'd', 'e': 'f'}) == {'b': 'a', 'd': 'c', 'f': 'e'}


"""Tests favorite_color function."""


def test_favorite_color1() -> None:
    """To test that when there is a tie, it returns color that appeared first."""
    assert favorite_color({'Gigi': 'yellow', 'Iman': 'blue', 'Scott': 'blue', 'Ayah': 'yellow'}) == "yellow"


def test_favorite_color2() -> None:
    """To test for empty string."""
    assert favorite_color({'Gigi': '', 'Iman': '', 'Scott': 'blue'}) == ""


def test_favorite_color3() -> None:
    """To test for winning color with 4 people and 3 colors."""
    assert favorite_color({'Gigi': 'yellow', 'Iman': 'blue', 'Scott': 'blue', 'Ayah': 'pink'}) == "blue"


"""Tests count function."""


def test_count1() -> None:
    """To count 3 items."""
    assert count(["A", "B", "C", "C", "C"]) == {'A': 1, 'B': 1, 'C': 3}


def test_count2() -> None:
    """To count 4 items."""
    assert count(["A", "B", "C", "C", "C", "D", "D"]) == {'A': 1, 'B': 1, 'C': 3, 'D': 2}


def test_count3() -> None:
    """To count 1 item."""
    assert count(["A", "A", "A"]) == {'A': 3}