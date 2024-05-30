from is_anagram import Solution

def test_is_anagram():
    test_cases = [
        (1, 'anagram', 'nagaram', True),
        (2, 'rat', 'car', False),
        (3, 'a', 'ab', False),
        (4, 'a', 'aa', False),
        (5, 'aacc', 'ccac', False),
        (6, 'aa cc d', 'dc ca a', True),
        (7, 'aa ccd', 'dc ca  a', False)
    ]

    for num, str1, str2, expected in test_cases:
        s = Solution()
        assert s.is_anagram(str1, str2) == expected, f"failed test #{num}: {str1} vs. {str2}"


if __name__ == "__main__":
    test_is_anagram()