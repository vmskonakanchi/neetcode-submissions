class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)

        res = [0] * n
        left = 1

        for i in range(n):
            res[i] = left
            left *= nums[i]

        right = 1
        res2 = [0] * n
        
        for i in range(n - 1,-1,-1):
            res2[i] = right
            right *= nums[i]

        for i in range(n):
            res[i] *= res2[i]

        return res