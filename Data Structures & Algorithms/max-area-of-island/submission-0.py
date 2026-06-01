class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        max_area_island = 0
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(dr + r, dc + c)

            return area
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area_island = max(max_area_island, dfs(row, col))
        return max_area_island