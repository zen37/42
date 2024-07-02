#Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def length(self, s: str) -> int:
        chars = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.length("abccggggg"))