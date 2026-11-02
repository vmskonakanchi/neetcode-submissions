class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1

        while l != r:
            if nums[l] > nums[r]:
                l += 1
            else:
                r -= 1

        return nums[l]