from container import Solution

test_cases = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1)
]

def test_max_area_1():
    s = Solution()
    for height, expected in test_cases:
        result = s.max_area_1(height)
        assert result == expected, "FAIL"
