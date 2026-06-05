class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)

        result = []

        for freq in range(len(buckets) - 1,-1,-1):
            num_list = buckets[freq]

            if len(result) == k:
                break

            for num in num_list:
                result.append(num)

        return result