from speed import Solution
test_cases = [
    ([3,6,7,11], 8, 4),
    ([30,11,23,4,20], 6, 23),
    ([30,11,23,4,20], 5, 30)
]

def test_determine_minimum_speed():
    s = Solution()
    for test in test_cases:
        print(test)
        expected = test[2]
        result = s.speed_minimum(test[0], test[1])
        assert result == expected, f"FAIL for piles: {test[0]}, hour: {test[1]}, speed result: {result} vs expected: {expected}"
