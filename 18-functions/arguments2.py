from typing import Dict

def combine_dicts(*args:Dict[str, int]) -> Dict[str, int]:
    result = {}

    for arg in args:
        for key, value in arg.items():
            result[key] = result.get(key, 0) + value

    return result

def test_combine_dicts():
    test_cases = [
        ([{'a': 100, 'b': 200}, {'a': 200, 'c': 300}], {'a': 300, 'b': 200, 'c': 300}),
        ([{'a': 100, 'b': 200}, {'a': 200, 'c': 300}, {'a': 300, 'd': 100}], {'a': 600, 'b': 200, 'c': 300, 'd': 100}),
    ]

    # Using enumerate
    for i, (dicts, expected) in enumerate(test_cases):
        result = combine_dicts(*dicts)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"

    # Without enumerate
    for index in range(len(test_cases)):
        dicts, expected = test_cases[index]
        result = combine_dicts(*dicts)
        assert result == expected, f"Test case {index + 1} failed: expected {expected}, got {result}"

if __name__ == "__main__":
    test_combine_dicts()
    print("All tests passed.")
