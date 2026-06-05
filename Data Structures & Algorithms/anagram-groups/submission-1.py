class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_dict = {}

        for s in strs:
            sstr = "".join(sorted(s))
            word_group = words_dict.get(sstr,[])
            word_group.append(s)
            words_dict[sstr] = word_group

        return list(words_dict.values())