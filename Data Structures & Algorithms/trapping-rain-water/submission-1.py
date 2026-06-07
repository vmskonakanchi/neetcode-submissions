class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        most_water = 0

        for i in range(1, n - 1):
            max_left = max(height[0:i])
            max_right = max(height[i + 1 : n])
            water_trapped = min(max_left, max_right)
            most_water += max(0,water_trapped - height[i])

        return most_water
