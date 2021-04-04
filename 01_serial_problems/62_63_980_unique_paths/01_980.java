class Solution {
    public int uniquePathsIII(int[][] grid) {
        int count = 0;
        int start_row = -1;
        int start_col = -1;
        for (int i = 0; i < grid.length; ++i) {
            for (int j = 0; j < grid[0].length; ++j) {
                if (grid[i][j] >= 0) count++;
                if (grid[i][j] == 1) {
                    start_row = i;
                    start_col = j;
                }
            }
        }
        
        int[] path_count = new int[] {0};
        if (start_row >= 0 && start_col >= 0) {
            backtracking(grid, start_row, start_col, count, path_count);
        }
        
        return path_count[0];
    }
    
    private void backtracking(int[][] grid, int row, int col, int remaining, int[] total) {
        int[] dr = new int[] {0, 0, 1, -1};
        int[] dc = new int[] {1, -1, 0, 0};
        
        if (grid[row][col] == 2 && remaining == 1) {
            total[0] += 1;
            return;
        }
        
        int temp = grid[row][col];
        grid[row][col] = -4;
        remaining -= 1;
        
        for (int i = 0; i < 4; ++i) {
            int r = row + dr[i];
            int c = col + dc[i];
            
            if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] < 0) {
                continue;
            }
            
            backtracking(grid, r, c, remaining, total);
        }
        
        grid[row][col] = temp;
        
    }
}