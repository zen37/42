from buy_sell_stocks import Solution

test_cases = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0)
]


def test_determine_max_profit():
    s = Solution()
    for prices, expected in test_cases:
        result = s.max_profit(prices)
        assert result == expected, f"FAIL result {result} vs expected {expected}"