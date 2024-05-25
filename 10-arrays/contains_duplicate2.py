from typing import List

TEXT_RESPONSE = "list contains duplicates: "
MY_LIST = [1, 2, 7, 3]

class Solution:
    @staticmethod
    def contains_duplicate(nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False


if __name__ == "__main__":
    is_duplicate_in_list = Solution.contains_duplicate(MY_LIST)
    print(TEXT_RESPONSE, is_duplicate_in_list)