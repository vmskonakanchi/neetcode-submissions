class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # stores indices

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx

            stack.append(i)

        return result