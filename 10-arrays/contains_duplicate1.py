from typing import List
import timeit
from contains_duplicate_const import MY_LIST, EXECUTION_COUNT

"""
List[int] does not enforce the type of the elements in the list by itself.
"""
class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        nums_hashset = set() # O(1) operation

        for n in nums: # the loop runs max n times, so O(n) operation
            if n in nums_hashset: # O(1) operation, due to efficient nature of hashsets
                return True
            nums_hashset.add(n) # O(1) operation
        return False
'''
The time complexity O(n)⋅O(1)=O(n)
'''

def check():
    solution = Solution()
    is_duplicate_in_list = solution.contains_duplicate(MY_LIST)
    #print(TEXT_RESPONSE, is_duplicate_in_list)

if __name__ == "__main__":
    total_execution_time = timeit.timeit(check, number=EXECUTION_COUNT)
    total_execution_time_ms = total_execution_time * 1_000
    print(f"Total execution time: {total_execution_time_ms:.2f} milliseconds")