class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        num_map = {}
        for i in range(n):
            diff = target - nums[i]
            if diff in num_map:
                return [num_map[diff],i]
            num_map[nums[i]] = i

        return []