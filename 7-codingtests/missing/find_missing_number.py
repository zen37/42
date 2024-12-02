# if you had an unsorted set of numbers from 1 to n, with one number missing, how would you find the missing number
from typing import List

class Solution:
    def find_using_sum(self, nums: List[int]) -> int:
        sum_actual = sum(nums)

        n = len(nums) + 1 # expected count of numbers, +1 the missing one
        sum_expected = n * (n + 1) // 2   

        missing_num = sum_expected - sum_actual

        return missing_num if missing_num < max(set(nums)) else None
        
    
    def find_using_set(self, nums):
        n = len(nums) + 1  # n is the total count of numbers including the missing one
        expected_set = set(range(1, n + 1))
        actual_set = set(nums)

        missing_number = expected_set - actual_set

        missing_num = missing_number.pop()
        return None if actual_set and missing_num > max(actual_set) else missing_num

        #return missing_number.pop()  # pop the only element from the set
        #return missing_number[0]  # does not work, set has to be converted in list missing_number_list = list(missing_number)
    

if __name__ == "__main__":
    s = Solution()
    print(s.find_using_set([2, 1]))
    print(s.find_using_sum([2, 1]))