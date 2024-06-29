from search_2d_matrix import Solution, SolutionNeetcode

test_cases =[
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1, True),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], -33, False),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60, True),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1111, False),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 9, False),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 30, True)
]

def test_search_matrix():
    s = Solution()
    print()
    for test in test_cases:
        print(test)
        expected = test[2]
        result = s.searchMatrix(test[0], test[1])
        assert result == expected, f"FAIL for list: {test[0]}, target: {test[1]}, result: {result} vs expected: {expected}"

def test_search_matrix_neetcode():
    s = SolutionNeetcode()
    print()
    for test in test_cases:
        print(test)
        expected = test[2]
        result = s.searchMatrix(test[0], test[1])
        assert result == expected, f"FAIL for list: {test[0]}, target: {test[1]}, result: {result} vs expected: {expected}"