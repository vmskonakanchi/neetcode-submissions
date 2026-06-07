class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                curr_sum = numbers[i] + numbers[j]

                print(i,numbers[i],j,numbers[j],curr_sum)

                if curr_sum == target:
                    return [i + 1,j + 1]
        
        return []
        
