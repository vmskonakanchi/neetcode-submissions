class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        most_water = 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]

        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, n - 1):
            water_trapped = min(left_max[i], right_max[i])
            most_water += max(0, water_trapped - height[i])

        return most_water
