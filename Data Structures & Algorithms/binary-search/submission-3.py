class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            print(mid)
            cur = nums[mid]

            if cur == target:
                return mid
            elif cur > target:
                r -= 1
            elif cur < target:
                l += 1
            
        return -1