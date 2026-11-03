class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for idx,num in enumerate(nums):

            if (num - 1) not in num_set:
                cur = 1
                
                # we have a start of a seq
                while (num + cur) in num_set:
                    cur += 1
            
                longest = max(longest,cur)

        return longest

            