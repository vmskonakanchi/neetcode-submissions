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
            start = j + 1
            end = start + length

            result.append(s[start: end])
            i = end
            j = i + 1
        
        return result


