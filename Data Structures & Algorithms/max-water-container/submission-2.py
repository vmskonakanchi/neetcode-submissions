class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        most_water = 0

        while r > l:
            length = r - l
            height = min(heights[l],heights[r])
            area = height * length

            most_water = max(most_water,area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return most_water