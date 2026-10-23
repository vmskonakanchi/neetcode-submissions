class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [None] * (n + 1)

        for b in range(0,n + 1):
            output[b] = self.count_ones(format(b,'b'))

        return output


    def count_ones(self,b_string:str):
        count = 0

        for i in b_string:
            if i == '0':
                continue
            count += 1
        
        return count
