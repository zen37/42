from find_first_true import Solution

test_cases = [
    ([False, False, True], 2),
    ([False, False, True, True], 2),
    ([False, False, False, False, True], 4),
    ([False, False, False, False], -1),
    ([True, True, True], 0)
]


def test_find_first_true():
    s = Solution()
    print()
    for test in test_cases:
        expected = test[1]
        result = s.search(test[0])
        assert result == expected, f"FAIL for List: {test[0]}, result: {result} vs. expected {expected}]"
        print(f"PASS for List: {test[0]}, result: {result} == expected {expected}")