from typing import List

nums = [1, 2, 9]
target = 11

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None


class Solution2:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i

        return None 



        return None


if __name__ == "__main__":
    s = Solution2()
    print(s.twoSum(nums, target))
