import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_nums = []
        
        for n in nums:
            heapq.heappush(new_nums, n)
            if len(new_nums) > k:
                heapq.heappop(new_nums)

        return heapq.heappop(new_nums)