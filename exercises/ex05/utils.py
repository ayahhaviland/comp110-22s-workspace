"""EX 05 - List Utils."""

__author__ = "730236204"


def only_evens(numbers: list[int]) -> list[int]:
    """A function to return even numbers from a list."""
    even_numbers = []
    i = 0
    while i < len(numbers):
        if (numbers[i] % 2 == 0):
            even_numbers.append(numbers[i])
        i += 1
    return even_numbers


def sub(num_list: list[int], first_index: int, last_index: int) -> list[int]:
    """A function to return a list which is a subset of the given list, between the specified start index and the end index - 1."""
    sub_list = []
    x = first_index - 1
    while x < (last_index - 1):
        sub_list.append(num_list[x + 1])
        x += 1
    return sub_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """A function to return a list of 2 inputed lists."""
    concat_list = []
    y = 0
    while y < len(first_list):
        concat_list.append(first_list[y])
        y += 1
    y = 0
    while y < len(second_list):
        concat_list.append(second_list[y])
        y += 1
    return concat_list