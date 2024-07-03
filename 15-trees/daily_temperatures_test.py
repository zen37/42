from daily_temperatures import Solution

test_cases = [
    ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
    ([30,40,50,60], [1,1,1,0]),
    ([30,60,90], [1,1,0])
]


def test_daily_temperatures():

    s = Solution()
    for input, expected in test_cases:
        result = s.dailyTemperatures(input)
        assert result == expected, "FAIL"
