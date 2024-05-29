from is_reverse import *

def test_is_reverse():
    test_cases = [
        (1, "d rac", "car d", True),
        (2, "hello", "olleh", True),
        (3, "python", "nohtyp", True),
        (4, "example", "elpmaxe", True),
        (5, "test", "tset", True),
        (6, "not", "reverse", False),
        (7, "palindrome", "emordnilap", True)
    ]
    for num, str1, str2, expected in test_cases:
        assert Solution.is_reverse(str1, str2) == expected, f"Failed for test #{num}: {str1} and {str2}"


if __name__ == "__main__":
    test_is_reverse()
