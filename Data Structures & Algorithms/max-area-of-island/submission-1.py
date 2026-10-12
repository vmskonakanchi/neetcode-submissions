class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        current_area = 0
        visited = set()

        def dfs(idx_r,idx_c):
            if idx_r < 0 or idx_r >= rows or idx_c < 0 or idx_c >= cols:
                return 0

            item = grid[idx_r][idx_c]

            if item == 0:
                return 0

            key = (idx_r,idx_c)

            if key in visited:
                return 0

            visited.add(key)
            
            return 1 + (
                dfs(idx_r + 1,idx_c) +
                dfs(idx_r - 1,idx_c) +
                dfs(idx_r,idx_c + 1) +
                dfs(idx_r,idx_c - 1)
            )


        for r in range(rows):
            for c in range(cols):
                current_area += dfs(r,c)
                max_area = max(current_area, max_area)
                current_area = 0

        return max_area