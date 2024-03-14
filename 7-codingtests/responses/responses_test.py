import pytest
from responses import getWrongAnswers

@pytest.mark.parametrize("N, C, expected", [
    (1, "A", "B"),
    (3, "ABA", "BAB"),
    (0, "", ""),
    (4, "BBBB", "AAAA")
])
def test_getWrongAnswers(N, C, expected):
    assert getWrongAnswers(N, C) == expected
