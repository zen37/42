from typing import List

class Solution():
    def max_area_1(self, height: List[int]) -> int:
        
        result = 0

        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min (height[l], height[r])
                result = max(result, area)

        return result