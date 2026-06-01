class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums_dict = {}

        for i in range(len(nums)):
            check = target - nums[i]
            if check in sums_dict:
                return [sums_dict[check],i]

            sums_dict[nums[i]] = i
        


        