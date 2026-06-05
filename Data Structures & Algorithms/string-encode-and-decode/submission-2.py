class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "#" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 1
        result = []

        while i < len(s):
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1: (j + 1) + length])
            i = j + length + 1
            j = i + 1
        
        return result


