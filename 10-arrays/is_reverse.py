
class Solution:
    @staticmethod
    def is_reverse(s:str, t:str) -> bool:
        reversed_string = ''.join(reversed(t))
        return s == reversed_string

if __name__ == "__main__":
    str1 = "anagram"
    str2 = "margana"
    print(Solution.is_reverse(str1, str2))