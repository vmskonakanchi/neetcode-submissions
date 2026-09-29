class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_map = set()

        for n in nums:
            if n in num_map:
                num_map.remove(n)
            else:
                num_map.add(n)
        
        return list(num_map)[0]
            

