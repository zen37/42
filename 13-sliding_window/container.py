from typing import List

class Solution():
    def max_area_1(self, height: List[int]) -> int:
        
        result = 0

        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min (height[l], height[r])
                result = max(result, area)

        return result
    
    def max_area_2(self, height: List[int]) -> int:
        
        result = 0

        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min (height[l], height[r])
            result = max(result, area)

            """
            if height[l] < height [r]:
                l = l + 1
            elif height[r] < height[l]:
                r = r - 1
            else:
                l = l + 1
            """
            if height[r] < height[l]:
                r = r - 1
            else:
                l = l + 1

        return result