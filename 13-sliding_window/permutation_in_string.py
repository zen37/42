# https://leetcode.com/problems/permutation-in-string/description/

"""
checkInclusion_1
Runtime 4710 ms Beats 5.00%
Memory 16.50 MB Beats 98.26%

Runtime 4710 ms Beats 5.00%
Memory 16.50 MB Beats 88.83%
"""


class Solution:
    def checkInclusion_1(self, s1: str, s2: str) -> bool:

        map_s1 = {}

        for c in s1:
            if c in map_s1:
                map_s1[c] = map_s1[c] + 1
            else:
                map_s1[c] = 1
        
        for i in range(len(s2)):
            s2_sub = s2[i:i+len(s1)]
            #print(s2_sub)
            map_s2_sub = {}
            for c in s2_sub:
                if c in map_s2_sub:
                    map_s2_sub[c] = map_s2_sub[c] + 1
                else:
                    map_s2_sub[c] = 1
            if map_s1 == map_s2_sub:
                return True


        return False



s = Solution()
print(s.checkInclusion_1("ab", "eidbaooo"))
print(s.checkInclusion_1("ab", "eidboaoo"))
