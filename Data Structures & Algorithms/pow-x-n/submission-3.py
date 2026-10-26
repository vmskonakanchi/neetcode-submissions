class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = self.helper(x,abs(n))
        return res if n > 0 else 1 / res
    
    
    def helper(self,x,n):
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = self.helper(x * x, n // 2)

        if n % 2 == 0: # even
            return res
        else:
            return x * res