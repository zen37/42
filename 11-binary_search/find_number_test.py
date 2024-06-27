from find_number import Solution

test_cases = [
    ([1, 2, 7, 9], 4, -1),
    ([-1,0,3,5,9,12], 9, 4),
    ([-1,0,3,12], -1, 0)
]

def test_find_number():
    for nums, target, expected in test_cases:
        s = Solution()
        result = s.search(nums, target)
        assert result == expected, f"solution failed for list of numbers: {nums}, target: {target} ... result: {result} vs. expected {expected}"