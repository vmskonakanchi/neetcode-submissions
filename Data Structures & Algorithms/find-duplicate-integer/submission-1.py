class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_map = {}

        for n in nums:
            if n not in num_map:
                num_map[n] = 0
            else:
                return n

        return -1