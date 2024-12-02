from two_sum import Solution1, Solution2

def test_two_sum():
    test_cases = [
        ([2,7,11,15], 9, [0,1]),
        ([3,2,4], 6, [1,2]),
        ([3,3], 6, [0,1])
    ]

    for nums, target, expected in test_cases:
        s = Solution1()
        result = s.twoSum(nums, target)
        assert result == expected, f"Solution1 failed test #{nums, target}: {result} vs. {expected}"

        s = Solution2()
        result = s.twoSum(nums, target)
        assert result == expected, f"Solution2 failed test #{nums, target}: {result} vs. {expected}"