# https://leetcode.com/problems/daily-temperatures/

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        index_temp = [] # index and temperature
        
    
        for i, temp in enumerate(temperatures):
            while index_temp and temp > index_temp[-1][1]:
                index, temperature = index_temp.pop()
                res[index] = i - index
            index_temp.append((i, temp))
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([30,40,50,60]))