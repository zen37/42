from typing import List

nums = [1, 2, 7, 9]
target = 4

class Solution:
    def search(self, nums:List[int], target:int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1


if __name__ == "__main__":
    s = Solution()
    r = s.search(nums, target)
    print('result: ', r)