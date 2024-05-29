from is_anagram import *

def test():
    test_cases = [
        (1, 'anagram', 'nagaram', True),
        (2, 'rat', 'car', False)
    ]

    for num, str1, str2, expected in test_cases:
        solution = Solution()
        assert solution.is_anagram(str1, str2) == expected, f"failed test #{num}: {str1} vs. {str2}"