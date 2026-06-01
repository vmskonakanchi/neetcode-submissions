class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}

        for i in nums:
            if i in nums_dict:
                return True

            nums_dict[i] = True
            
        return False