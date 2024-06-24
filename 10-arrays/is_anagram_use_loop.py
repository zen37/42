from collections import Counter

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dict_s, dict_t  = {}, {}

        for i, char in enumerate(s):
            dict_s[char] = 1 + dict_s.get(char, 0)
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)


        for key in dict_s:
            if dict_s[key] != dict_t.get(key, 0):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.is_anagram("ss2a", "2saqs"))
