class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        queue = deque()
        fresh_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_count += 1
                if grid[row][col] == 2:
                    queue.append((row, col))

        if fresh_count == 0:
            return 0
        if not queue and fresh_count > 0:
            return -1
        minutes = 0
        while queue and fresh_count > 0:
            level_size = len(queue)
            for _ in range(level_size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            minutes += 1
        return minutes if fresh_count == 0 else -1



        


        # queue = deque()
        # fresh_count = 0

        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == 1:
        #             fresh_count += 1
        #         if grid[row][col] == 2:
        #             queue.append((row, col))

        # if fresh_count == 0:
        #     return 0
        # if not queue and fresh_count > 0:
        #     return -1
        
        # minutes = 0

        # while queue and fresh_count > 0:
        #     level_size = len(queue)
        #     for _ in range(level_size):
        #         r, c = queue.popleft()
        #         for dr, dc in directions:
        #             nr, nc = r + dr, c + dc
        #             if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
        #                 continue
                    
        #             # if it's a fresh fruit, rot it and enqueue it
        #             if grid[nr][nc] == 1:
        #                 grid[nr][nc] = 2
        #                 fresh_count -= 1
        #                 queue.append((nr, nc))

        #     # one full wave finished => one minute elapsed
        #     minutes += 1

        # # if fresh remains impossible     
        # return minutes if fresh_count == 0 else -1
        