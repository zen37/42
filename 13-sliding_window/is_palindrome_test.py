from is_palindrome import Solution

test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True)
]

def test_is_palindrome_1():
    s = Solution()
    
    for input, expected in test_cases:
        result = s.is_palindrome_1(input)
        assert result == expected, "FAIL"