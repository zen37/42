import time
from typing import List

nums = [1,2,1] * 1000000

"""
nums = [1,2,1] * 10000
concatenate took 0.000919 seconds
concatenate took 0.000400 seconds
concatenate took 0.001724 seconds

nums = [1,2,1] * 100000
concatenate took 0.012431 seconds
concatenate took 0.003559 seconds
concatenate took 0.035866 seconds

nums = [1,2,1] * 1000000
concatenate took 0.161403 seconds
concatenate took 0.072219 seconds
concatenate took 0.249328 seconds
"""

class Solution:
    def concatenate1(self, nums: List[int]) -> List[int]:
        ans = nums[:]
        for n in nums:
            ans.append(n)
        return ans

    def concatenate2(self, nums: List[int]) -> List[int]:
        return nums + nums

    def concatenate3(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans


if __name__ == "__main__":
    s = Solution()

    start = time.time()
    r = s.concatenate1(nums)
    end = time.time()
    print(f"concatenate took {end - start:.6f} seconds")

    start = time.time()
    r = s.concatenate2(nums)
    end = time.time()
    print(f"concatenate took {end - start:.6f} seconds")

    start = time.time()
    r = s.concatenate3(nums)
    end = time.time()
    print(f"concatenate took {end - start:.6f} seconds")