class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq_dict = defaultdict(bool)

        for n in nums:

            if n in uniq_dict:
                return True

            uniq_dict[n] = True

        return False
            