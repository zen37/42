from missing.find_missing_number import Solution

test_cases = [
    ([3, 2, 1, 5], 4),
    ([3, 7, 1, 2, 8, 4, 6], 5),
    ([3, 1], 2),
    ([2, 1], None),
    ([1], None)
]

def test_find_missing_number_1():
    s = Solution()
    for test in  test_cases:
        expected = test[1]
        result = s.find_using_sum(test[0])
        assert result == expected, f"FAIL {result} vs. {expected}"

def test_find_missing_number_2():
    s = Solution()
    for test in  test_cases:
        expected = test[1]
        result = s.find_using_set(test[0])
        assert result == expected, f"FAIL {result} vs. {expected}"