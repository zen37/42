# https://leetcode.com/problems/valid-parentheses/description/

class Solution():
    def isValid(self, s: str) -> bool:
        map = {")": "(", "]": "[", "}": "{"}
        list = []

        for c in s:
            if c not in map:
                list.append(c)
                continue
            if not list or list[-1] != map[c]:
                return False
            list.pop()

        return not list

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("{}"))
    print(s.isValid("(]"))
    print(s.isValid("()[]{}"))