class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        most_water = 0

        for i in range(1, n - 1):
            max_left = 0
            max_right = 0

            for l in range(0,i):
                if height[l] > max_left:
                    max_left = height[l]

            for r in range(i + 1,n):
                if height[r] > max_right:
                    max_right = height[r]

            water_trapped = min(max_left, max_right)
            most_water += max(0,water_trapped - height[i])

        return most_water
