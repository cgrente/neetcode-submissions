class Solution {
    public int orangesRotting(int[][] grid) {
        if (grid.length == 0) {
            return 0;
        }
        Queue<int[]> queue = new ArrayDeque<>();
        int fresh = 0;
        int minMinute = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        int[][] directions = {
            {-1, 0},
            {1, 0},
            {0, -1},
            {0, 1}
        };

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == 2) {
                    queue.offer(new int[]{row, col});
                } else if (grid[row][col] == 1) {
                    fresh += 1;
                }
            }
        }

        if (fresh == 0) {
            return 0;
        }

        while (!queue.isEmpty() && fresh > 0) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cell = queue.poll();
                for (int[] direction : directions) {
                    int row = cell[0] + direction[0];
                    int col = cell[1] + direction[1];
                    if (row >= 0 && row < rows && col >= 0 && col < cols && grid[row][col] == 1) {
                        grid[row][col] = 2;
                        fresh--;
                        queue.offer(new int[]{row, col});
                    }
                } 
            }
            minMinute++;
        }


        return fresh == 0 ? minMinute : -1;
    }
}