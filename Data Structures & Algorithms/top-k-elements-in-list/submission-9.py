class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n not in num_map:
                num_map[n] = 0
            num_map[n] += 1

        for num,cnt in num_map.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return []