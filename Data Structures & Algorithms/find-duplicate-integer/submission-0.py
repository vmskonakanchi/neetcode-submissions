class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_map = {}

        for n in nums:
            if n not in num_map:
                num_map[n] = 0

            num_map[n] += 1

        for k,v in num_map.items():
            if v > 1:
                return k

        return -1