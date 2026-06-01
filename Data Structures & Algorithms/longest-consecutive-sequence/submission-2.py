class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        length = 0

        for i in nums:
            # check if we have start of sequence
            if (i - 1) not in numsSet:
                # we have a start of seqence
                length = 1
                
                while (i + length) in numsSet:
                    length += 1
                
                longest = max(length,longest)

        return longest


