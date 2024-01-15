# test_main.py
import pytest
from constants import ONE, TWO, TIE
from main import who_won, valid

@pytest.mark.parametrize("input, expected", [
    ([1, 2, 1, 2, 1, 2], TIE),
    ([1, 2, 1, 2, 1], ONE),
    ([2, 1, 2, 1, 2], TWO),
])

def test_who_won(input, expected):
    result = who_won(input)
    assert result == expected

"""
def test_who_won_tie():
    result = who_won([1, 2, 1, 2, 1, 2])
    assert result == TIE

def test_who_won_one():
    result = who_won([1, 2, 1, 2, 1])
    assert result == ONE

def test_who_won_two():
    result = who_won([2, 1, 2, 1, 2])
    assert result == TWO
"""

def test_valid_with_valid_rounds():
    rounds = [1, 2, 1, 2, 1]
    result = valid(rounds)
    assert result is True

def test_valid_with_invalid_element():
    rounds = [1, 2, 3, 2, 1]
    result = valid(rounds)
    assert result is False

def test_valid_with_empty_list():
    rounds = []
    result = valid(rounds)
    assert result is False

def test_valid_with_both_invalid_and_empty_list():
    rounds = [3, 4, 5]
    result = valid(rounds)
    assert result is False

