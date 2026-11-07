from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        queue = deque([])

        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        queue.append((r + dr, c + dc, 1))

        while queue:
            r, c, dist = queue.popleft()
            if not in_bounds(r, c):
                continue
            if (r, c) in visited:
                continue
            if grid[r][c] == -1:
                continue

            visited.add((r, c))
            grid[r][c] = dist

            queue.append((r + 1, c, dist + 1))
            queue.append((r - 1, c, dist + 1))
            queue.append((r, c + 1, dist + 1))
            queue.append((r, c - 1, dist + 1))