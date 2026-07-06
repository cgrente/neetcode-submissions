class Solution {
    public int numIslands(char[][] grid) {
        if (grid.length == 0) {
            return 0;
        }

        int rows = grid.length;
        int cols = grid[0].length;
        int numberOfIsland = 0;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == '1') {
                    this.dfs(grid, row, col);
                    numberOfIsland++;
                }
            }
        }

        return numberOfIsland;
    }

    private void dfs(char[][] grid, int row, int col) {
        if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length || grid[row][col] == '0') {
            return;
        }

        grid[row][col] = '0';
        
        this.dfs(grid, row + 1, col);
        this.dfs(grid, row - 1, col);
        this.dfs(grid, row, col + 1);
        this.dfs(grid, row, col - 1);
    }
}
