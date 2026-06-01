class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = 0
        streak = 0
        res = 0

        nums.sort()
        i = 0
        
        while i < len(nums):
            if nums[i] != curr:
                curr = nums[i]
                streak = 0

            while i < len(nums) and nums[i] == curr:
                i += 1
            
            streak += 1
            curr += 1
            res = max(res,streak)

        return res

