class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_dict = {}
        second_dict = {}

        for i in s:
            first_dict[i] = first_dict.get(i,0) + 1

        for i in t:
            second_dict[i] = second_dict.get(i,0) + 1

        return first_dict == second_dict