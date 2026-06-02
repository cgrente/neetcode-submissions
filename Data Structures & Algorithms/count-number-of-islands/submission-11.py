class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        nb_of_island = 0
        def bfs(row, col):
            visited.add((row, col))
            
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if grid[nr][nc] == '1' and (nr, nc) not in visited:
                    bfs(nr, nc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    nb_of_island += 1
                    bfs(row, col)

        return nb_of_island