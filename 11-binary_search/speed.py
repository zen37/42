import math
from typing import List

class Solution:
    def speed_minimum(self, piles:List[int], hours:int)->int:

        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid_speed = (l + r) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / mid_speed)
            if total_time <= hours:
                res = mid_speed
                r = mid_speed - 1
            else:
                l = mid_speed + 1

        return res


if __name__ == '__main__':
    p = [30,11,23,4,20]
    h = 6
    s = Solution()
    result = s.speed_minimum(p, h)
    print(result)

