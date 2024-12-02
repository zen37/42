from collections import Counter

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
    #def is_anagram(self, s,t):   #works too
        return Counter(s) == Counter(t)
'''
Time complexity:
Time to construct Counter(s): O(n)Time to construct Counter(t): O(m)
Total time O(max(n, m)+k), k is the number of unique characters in s and t

Space complexity:
O(k1 + k2), where k1 and k2 are the number of unique characters in strings s and t, respectively.
'''

if __name__ == "__main__":
    solution = Solution()
    print(solution.is_anagram("ss2a", "2sas"))
