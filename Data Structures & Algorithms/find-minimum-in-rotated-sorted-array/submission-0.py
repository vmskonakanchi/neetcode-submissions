class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        cur_min = nums[0]

        for n in range(1,len(nums)):
            if nums[n] < cur_min:
                cur_min = nums[n]

        return cur_min