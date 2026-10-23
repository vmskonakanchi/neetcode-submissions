class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [None] * (n + 1)

        for b in range(0,n + 1):
            output[b] = bin(b).count('1')

        return output