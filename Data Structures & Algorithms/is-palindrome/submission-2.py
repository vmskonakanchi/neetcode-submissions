class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for c in s:
            if c.isalnum():
                new_str += c.strip().lower()

        print(new_str,new_str[::-1])

        return new_str == new_str[::-1]