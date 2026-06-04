class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_dict = {}
        t_char_dict = {}

        for c in s:
            s_char_dict[c] = s_char_dict.get(c,0) + 1

        for c in t:
            t_char_dict[c] = t_char_dict.get(c,0) + 1

        return s_char_dict == t_char_dict
        