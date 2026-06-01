class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or grid[0] is None:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        visited = set()

        def dfs(row, col):
            visited.add((row, col))
            for r, c in directions:
                nr, nc = row + r, col + c
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if grid[nr][nc] == '1' and (nr, nc) not in visited:
                    dfs(nr, nc)

        nb_island = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs(row, col)
                    nb_island += 1

        ## DFS
        # def dfs(s_row: int, s_col: int) -> None:
        #     visited.add((s_row, s_col))
        #     for dr, dc in directions:
        #         nr, nc = dr + s_row, dc + s_col
        #         if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
        #             continue
        #         if grid[nr][nc] == '1' and (nr, nc) not in visited:
        #             dfs(nr, nc)

        # nb_island = 0
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == '1' and (row, col) not in visited:
        #             nb_island += 1
        #             dfs(row, col)

        ## BFS
        # def bfs(s_row, s_col):
        #     queue = deque()
        #     queue.append((s_row, s_col))
        #     visited.add((s_row, s_col))
        #     for dr, dc in directions:
        #         nr, nc = dr + s_row, dc + s_col
        #         if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
        #             continue
        #         if grid[nr][nc] == '1' and (nr, nc) not in visited:
        #             bfs(nr, nc)
        # nb_island = 0
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == '1' and (row, col) not in visited:
        #             nb_island += 1
        #             bfs(row, col)
        
        
        return nb_island