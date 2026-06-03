class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid[0]:
            return 0

        nb_island = 0

        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == "1" and (nr, nc) not in visited:
                        queue.append((nr, nc));
                        visited.add((nr, nc))
    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    nb_island += 1
                    bfs(row, col)

        return nb_island