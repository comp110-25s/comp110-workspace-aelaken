__author__: str = "730666919"
""" tests the functions that I just wrote

Author: Adam Laken """


from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest


__author__: str = "730666919"
""" tests the functions that I just wrote

Author: Adam Laken """


from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest


def test_invert1() -> None:
    """tests the invert function"""
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_invert2() -> None:
    """tests the invert function"""
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}


def test_invert3() -> None:
    """tests the invert function as an edge case"""
    with pytest.raises(KeyError):
        invert({"a": "b", "c": "b"})


def test_favorite_color1() -> None:
    """tests the favorite color function"""
    assert favorite_color({"a": "b", "c": "b"}) == "b"


def test_favorite_color2() -> None:
    """tests the favorite color function"""
    assert favorite_color({"a": "b", "c": "d", "e": "f"}) == "b"


def test_favorite_color3() -> None:
    """tests the favorite color function with edge case"""
    names_and_colors = {"Adam": "blue"}
    favorite_single = favorite_color(names_and_colors)
    assert favorite_single == "blue"


def test_count1() -> None:
    """tests the count function"""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count2() -> None:
    """tests the count function"""
    input_list3 = []
    counted_empty = count(input_list3)
    assert counted_empty == {}


def test_count3() -> None:
    """tests the count function"""
    assert count(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}


def test_bin_len1() -> None:
    """tests the bin_len function"""
    assert bin_len(["a", "bb", "ccc"]) == {1: {"a"}, 2: {"bb"}, 3: {"ccc"}}


def test_bin_len2() -> None:
    """tests the bin_len function"""
    assert bin_len(["a", "b", "cc", "dd", "eee", "fff"]) == {
        1: {"a", "b"},
        2: {"cc", "dd"},
        3: {"eee", "fff"},
    }


def test_bin_len3() -> None:
    """tests the bin_len function edge case"""
    assert bin_len([]) == {}
