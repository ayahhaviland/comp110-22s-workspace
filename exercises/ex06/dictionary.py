"""EX 06 - Dictionaries."""

__author__ = "730236204"


def invert(first_d: dict[str, str]) -> dict[str, str]:
    """To invert the keys and the values of a given dictionary."""
    # creating empty dictionary
    inverted_d: dict[str, str] = {}
    # loop for identifying components within first_d
    for key, value in first_d.items():
        # checking to see if value is already defined within inverted dictionary
        if value not in inverted_d.keys():
            # establish value as a key in the inverted dictionary
            inverted_d[value] = []
            # assign value currently in key to key of value in the inverted dictionary
            inverted_d[value] = key
        else:
            raise KeyError
    return inverted_d


def favorite_color(name_color: dict[str, str]) -> str:
    """To return a str which is the color that appears most frequently in a given dictionary."""
    most_frequent: dict[str, int] = {}
    # establishing integer variable to recieve current value for each dictionary entry
    color_count = int
    # loop for identifying components within name_color
    for key, value in name_color.items():
        # checking to see if the color is already in the most frequent dictionary
        if value not in most_frequent.keys():
            # establish color within most frequent dictionary to keep track of how many times each color appears
            most_frequent[value] = 1
        else:
            # if the color is already in the dictionary, increment the count by 1
            color_count = most_frequent[value]
            most_frequent[value] = color_count + 1
    # establishing variables to track color with highest use count
    max_color_name: str = ""
    max_color_count = 0
    # loop for identifying components of most frequent dictionary
    for key, value in most_frequent.items():
        # comparing the count of the current color against the highest
        if value > max_color_count:
            # if the current value is higher than the highest, then set color name and count to the max color name and max color count
            max_color_name = key
            max_color_count = value
    return max_color_name


def count(input_list: list[str]) -> dict[str, int]:
    """To produce a dictionary where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list from a given list."""
    # 1. Establish an empty dictionary to store your built-up result in
    resulting_dict: dict[str, int] = {}
    # variable to keep track of frequency of value
    current_value: int = 0
    # loop to see if that value has already been established as a key in your dictionary
    for key in input_list:  
        # means there is already a key/value pair where the value is a key
        if key in resulting_dict:  
            current_value = resulting_dict[key]
            resulting_dict[key] = current_value + 1
        # means value is not found in the dict so initializing to 1
        else:
            # adds new key
            resulting_dict[key] = []
            # initializes new key to 1
            resulting_dict[key] = 1
    return resulting_dict