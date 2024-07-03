class Solution:
    def is_palindrome_1(self, s: str) -> bool:
        s_new = ""

        for c in s:
            if c.isalnum():
                s_new += c.lower()

        return s_new == s_new[::-1]
    
    def is_palindrome_2(self, s:str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l = l + 1
            r = r - 1

        return True