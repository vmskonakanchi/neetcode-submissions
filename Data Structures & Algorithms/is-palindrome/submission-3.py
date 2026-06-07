class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for c in s:
            if c.isalnum():
                new_str += c.lower()

        l,r = 0,len(new_str) - 1

        while r > l:
            if new_str[l] != new_str[r]:
                return False
            l += 1
            r -= 1

        return True