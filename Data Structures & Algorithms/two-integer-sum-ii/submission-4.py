class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l , r = 0 , n - 1

        while r > l:
            num = numbers[l] + numbers[r]

            if num == target:
                return [l + 1, r + 1]
            elif num < target:
                l += 1
            elif num > target:
                r -= 1
        
        return []
        
