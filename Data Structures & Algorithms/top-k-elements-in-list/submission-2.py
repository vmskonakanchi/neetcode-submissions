class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            res[i] = res.get(i,0) + 1

        for n, c in res.items():
            freq[c].append(n)

        result = []
        
        for i in range(len(freq) - 1,0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

        return result
