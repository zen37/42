from contains_duplicate1 import Solution

def test_contains_duplicate_with_duplicates():
    # Test case with a list containing duplicates
    my_list = [1, 2, 7, 3, 2, 1]
    solution = Solution()
    assert solution.contains_duplicate(my_list) == True

def test_contains_duplicate_without_duplicates():
    # Test case with a list without duplicates
    my_list = [1, 2, 3, 4, 5]
    solution = Solution()
    assert solution.contains_duplicate(my_list) == False

def test_contains_duplicate_empty_list():
    # Test case with an empty list
    my_list = []
    solution = Solution()
    assert solution.contains_duplicate(my_list) == False
