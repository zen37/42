#Given a string s, find the length of the longest substring without repeating characters.
#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def length_prints(self, s: str) -> int:
        chars = set()
        l = 0
        res = 0

        for r in range(len(s)):
            print(f"s[r] is s[{r}]=", s[r])

            while s[r] in chars:
                print(f"s[r]={s[r]} found in {chars}")
                chars.remove(s[l])
                print(f"{s[l]} that is s[l]=s[{l}] removed from chars")
                print(f"set chars is now {chars}")
                l += 1
                print("left pointer increased by 1 is now",l)
                print("___end while_____")

            chars.add(s[r])
            print(f"chars after adding s[r]={s[r]}:", chars)
            res = max(res, r - l + 1)
            print(f"longest substring is max of {res} and {r-l+1}, that is (r-l+1)")
            print(f"___end for {r}_____")

        return res
    

    def length(self, s: str) -> int:
        
        set_chars = set()
        left = 0

        result = 0

        for right in range(len(s)):
 
            while s[right] in set_chars:
                set_chars.remove(s[left])
                left += 1

            set_chars.add(s[right])
            result = max(result, (right - left +1))

        return result


if __name__ == "__main__":
    s = Solution()
    r = s.length("wacbcb")
    print(f"longest substring without repeating characters: {r}")