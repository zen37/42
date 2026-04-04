import pytest

from main import (
    highest_product_sort,
    highest_product_islice,
    highest_product_index,
)


FUNCTIONS = [
    highest_product_sort,
    highest_product_islice,
    highest_product_index,
]


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2], 2),
        ([1, 2, 3, 4], 12),
        ([-10, -3, 1, 2], 30),
        ([-10, -3, -2, -1], 30),
        ([0, 5, 10], 50),
        ([5, 5, 1, 9], 45),
        ([-100_000, 100_000, 99_999], 9_999_900_000),
    ],
)
def test_highest_product_known_cases(numbers, expected):
    for function in FUNCTIONS:
        assert function(numbers) == expected


@pytest.mark.parametrize(
    "numbers",
    [
        [],
        [1],
    ],
)
def test_raises_value_error_for_too_short_input(numbers):
    for function in FUNCTIONS:
        with pytest.raises(ValueError):
            function(numbers)


@pytest.mark.parametrize(
    "numbers",
    [
        [3, 7, 2, 9, 4],
        [-10, -20, 1, 3, 2],
        [-5, -4, -3, -2],
        [0, 0, 0, 1],
        [8, -9, 10, -11, 3],
    ],
)
def test_all_implementations_match(numbers):
    results = [function(numbers) for function in FUNCTIONS]
    assert results[0] == results[1] == results[2]
