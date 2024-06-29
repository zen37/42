from typing import List

class Solution:
    def search(self, arr: List[bool], debug: bool = False) -> int:
        left, right = 0, len(arr) - 1
        if debug: print("left, right: ", left, right)
        if debug: counter = 0
        first_true_index = -1
        while left <= right:
            if debug: counter += 1; print(counter, " while ... ")
            mid = (left + right) // 2
            if debug: print("mid, arr[mid]", mid, arr[mid])
            if arr[mid]:
                first_true_index = mid
                if debug: print("first_true_index: ", first_true_index)
                right = mid -1
                if debug: print("right decreased by 1: ", right)
            else:
                left = mid + 1
                if debug: print("left increased by 1: ", left)
        if debug: print("exit while")

        return first_true_index

def print_result(index: int):
    if index != -1:
        print(f"First True found in position: {index}")
    else:
        print("True not found")
    print("____________________________________")


if __name__ == "__main__":
    s = Solution()
    index_first_true = s.search([False, False, True])
    print_result(index_first_true)
    index_first_true  = s.search([False, False, False], True)
    print_result(index_first_true)
    index_first_true  = s.search([False, True, True], True)
    print_result(index_first_true)
    index_first_true  = s.search([True, True, True], True)
    print_result(index_first_true)
