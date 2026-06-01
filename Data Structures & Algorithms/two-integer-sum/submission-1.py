class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums_dict = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in sums_dict:
                return [sums_dict[diff],i]
            sums_dict[n] = i

        return []
