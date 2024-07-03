class Solution:
    def is_palindrome_1(self, s: str) -> bool:
        s_new = ""

        for c in s:
            if c.isalnum():
                s_new += c.lower()

        return s_new == s_new[::-1]