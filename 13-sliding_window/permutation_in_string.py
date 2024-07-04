# https://leetcode.com/problems/permutation-in-string/description/

"""
checkInclusion_1
Runtime 4710 ms Beats 5.00%
Memory 16.50 MB Beats 98.26%

Runtime 4710 ms Beats 5.00%
Memory 16.56 MB Beats 88.83%

checkInclusion_2
Runtime 57ms Beats 70.19%
Memory 16.56 MB Beats 88.83%
"""


class Solution:
    def checkInclusion_1(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2) : return True

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

    def checkInclusion_2(self, s1: str, s2: str) -> bool:
            if len(s1) > len(s2):
                return False

            s1Count, s2Count = [0] * 26, [0] * 26
            for i in range(len(s1)):
                s1Count[ord(s1[i]) - ord("a")] += 1
                s2Count[ord(s2[i]) - ord("a")] += 1

            matches = 0
            for i in range(26):
                matches += 1 if s1Count[i] == s2Count[i] else 0

            l = 0
            for r in range(len(s1), len(s2)):
                if matches == 26:
                    return True

                index = ord(s2[r]) - ord("a")
                s2Count[index] += 1
                if s1Count[index] == s2Count[index]:
                    matches += 1
                elif s1Count[index] + 1 == s2Count[index]:
                    matches -= 1

                index = ord(s2[l]) - ord("a")
                s2Count[index] -= 1
                if s1Count[index] == s2Count[index]:
                    matches += 1
                elif s1Count[index] - 1 == s2Count[index]:
                    matches -= 1
                l += 1
            return matches == 26


s = Solution()
print("1st solution:")
print(s.checkInclusion_1("ab", "eidbaooo"))
print(s.checkInclusion_1("ab", "eidboaoo"))
print(s.checkInclusion_1("ab", "abc"))
print("\n")
print("2nd solution:")
print(s.checkInclusion_2("ab", "eidbaooo"))
print(s.checkInclusion_2("ab", "eidboaoo"))
print(s.checkInclusion_2("ab", "abc"))
