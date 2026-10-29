class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nl = len(nums)
        res = []
        
        for n in range(nl):
            if nums[n] > 0:
                break
            
            if n > 0 and nums[n] == nums[n - 1]:
                continue

            l , r = n + 1, nl - 1

            while l < r:
                result = nums[n] + nums[l] + nums[r]
                if result == 0:
                    res.append([nums[n], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif result < 0:
                    l += 1
                elif result > 0:
                    r -= 1

        return res