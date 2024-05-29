
class Solution:
    @staticmethod
    def is_reverse(s:str, t:str) -> bool:
        reversed_string = ''.join(reversed(t))
        print(reversed_string)
        if s == ''.join(reversed(t)):
            return True
        else:
            return False

if __name__ == "__main__":
    str1 = "anagram"
    str2 = "margana"
    print(Solution.is_reverse(str1, str2))