class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_s_dict = {}
        char_t_dict = {}

        for c in s:
            char_s_dict[c] = char_s_dict.get(c,0) + 1

        for c in t:
            char_t_dict[c] = char_t_dict.get(c,0) + 1

        return char_s_dict == char_t_dict