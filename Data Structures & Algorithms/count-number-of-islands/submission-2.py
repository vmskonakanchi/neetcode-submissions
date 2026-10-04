class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def lookAt(r,c,visited):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return
            if (r,c) in visited:
                return

            visited.add((r,c))

            if grid[r][c] == '0':
                return

            lookAt(r + 1,c,visited)
            lookAt(r - 1,c,visited)
            lookAt(r,c + 1,visited)
            lookAt(r,c - 1,visited)

        main_visited = set()
        total_count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                cur = grid[r][c]
                if cur == '0' or (r, c) in main_visited:
                    continue
                
                lookAt(r,c,main_visited)
                total_count += 1

        return total_count
