from typing import List
import timeit
from contains_duplicate_const import MY_LIST, EXECUTION_COUNT

class Solution:
    @staticmethod
    def contains_duplicate(nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False

def check():
    is_duplicate_in_list = Solution.contains_duplicate(MY_LIST)
    #print(TEXT_RESPONSE, is_duplicate_in_list)

if __name__ == "__main__":
    total_execution_time = timeit.timeit(check, number=EXECUTION_COUNT)
    total_execution_time_ms = total_execution_time * 1_000
    print(f"Total execution time: {total_execution_time_ms:.2f} milliseconds")