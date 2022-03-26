"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730236204"

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    
    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    dic_lis = ()

    for key, value in table.items():
        dic_lis = list(value)
        lis_idx = 0
        lis_max = rows
        if len(dic_lis) < lis_max:
            lis_max = len(dic_lis)
        # result[key] is a list to append to
        result[key] = []
        while lis_idx < lis_max:
            result[key].append(value[lis_idx])
            lis_idx += 1

    return result


def select(table: dict[str, list[str]], column: list[str]) -> dict[str, list[str]]:
    """Produce a new table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    
    for key, value in table.items():
        dic_lis = list(value)
        # checking to see if key is one of the included columns
        inc_col = "no"
        col_idx = 0
        while col_idx < len(column):
            if key == column[col_idx]:
                inc_col = "yes"
            col_idx += 1
        if inc_col == "yes":
            lis_idx = 0
        # result[key] is a list to append to
            result[key] = []
            while lis_idx < len(dic_lis):
                result[key].append(value[lis_idx])
                lis_idx += 1
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two column-based tables into one table."""
    result: dict[str, list[str]] = {}

    for key, value in table1.items():
        dic_lis = list(value)
        # checking to see if key is one of the included columns
        lis_idx = 0
        # result[key] is a list to append to
        result[key] = []
        while lis_idx < len(dic_lis):
            result[key].append(value[lis_idx])
            lis_idx += 1
    for key, value in table2.items():
        dic_lis = list(value)
        # checking to see if key is one of the included columns
        lis_idx = 0
        # result[key] is a list to append to
        result[key] = []
        while lis_idx < len(dic_lis):
            result[key].append(value[lis_idx])
            lis_idx += 1
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """To produce a dictionary where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list from a given list."""
    # 1. Establish an empty dictionary to store your built-up result in
    resulting_dict = {}
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