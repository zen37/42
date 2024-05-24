from typing import List

TEXT_RESPONSE = "list contains duplicates: "
MY_LIST = [1, 2, 7, 3]

"""
List[int] does not enforce the type of the elements in the list by itself.
"""
class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        nums_hashset = set()

        for n in nums:
            if n in nums_hashset:
                return True
            nums_hashset.add(n)
        return False

if __name__ == "__main__":
    solution = Solution()
    is_duplicate_in_list = solution.contains_duplicate(MY_LIST)
    print(TEXT_RESPONSE, is_duplicate_in_list)