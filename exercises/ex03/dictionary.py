__author__: str = "730666919"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """inverts the key and value of a user placed dictionary"""
    inverted_dict: dict[str, str] = {}  # type: ignore

    for key, value in input_dict.items():
        """checks if the value will be repeated twice as a key"""
        if value in inverted_dict:
            raise KeyError(f"Duplicate value found: {value}")
        inverted_dict[value] = key

    return inverted_dict


def count(input_list: list[str]) -> dict[str, int]:
    """creates a dictionary that organizes the number of
    times something appears in the list"""
    empty_dict: dict[str, int] = {}

    for item in input_list:
        if item in empty_dict:
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1

    return empty_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """gets list of favorite colors and counts the one with highest frequency"""

    color_counts = {}

    for name, color in input_dict.items():
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    input_dict = None
    count = -1

    for color, color_count in color_counts.items():
        if color_count > count:
            input_dict = color
            count = color_count

    return input_dict


def bin_len(bin_list: list[str]) -> dict[int, set[str]]:
    """bins a list of strings in a dictionary"""
    result_dict = {}

    for string in bin_list:
        length = len(string)

        if length not in result_dict:
            result_dict[length] = set()

        result_dict[length].add(string)

    return result_dict
