class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        most_water = 0

        left_max = height[0]
        right_max = height[n - 1]

        l, r = 1, n - 1

        while r >= l:
            if left_max < right_max:
                left_max = max(left_max, height[l])
                most_water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                most_water += right_max - height[r]
                r -= 1

        return most_water
