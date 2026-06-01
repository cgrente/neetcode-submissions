class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
        visited = set()

        def bfs(s_row, s_col):
            queue = deque()
            queue.append((s_row, s_col))
            visited.add((s_row, s_col))
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nc < 0 or nc >= cols or nr < 0 or nr >= rows:
                        continue
                    if grid[nr][nc] == '1' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr,nc))
                        

        number_of_islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    number_of_islands += 1
                    bfs(row, col)
        
        return number_of_islands


        # if len(grid) == 0 or len(grid[0]) == 0:
        #     return 0

        # rows = len(grid)
        # cols = len(grid[0])

        # visited = set()
        # directions = [
        #     (-1, 0),
        #     (0, -1),
        #     (1, 0),
        #     (0, 1)
        # ]

        # def bfs(s_row: int, s_col: int) -> None:
        #     queue = deque()
        #     queue.append((s_row, s_col))
        #     visited.add((s_row, s_col))
        #     while queue:
        #         r, c = queue.popleft()
        #         for dr, dc in directions:
        #             nr, nc = r + dr, c + dc
                    
        #             # in_bound check
        #             if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
        #                 continue
        #             if grid[nr][nc] == '1' and (nr, nc) not in visited:
        #                 visited.add((nr, nc))
        #                 queue.append((nr, nc))

        # nb_island = 0
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == '1' and (row, col) not in visited:
        #             nb_island += 1
        #             bfs(row, col)

        # return nb_island