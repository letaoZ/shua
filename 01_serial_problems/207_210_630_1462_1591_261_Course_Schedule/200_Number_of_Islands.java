class Solution {
    public int numIslands(char[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        boolean[][] visited = new boolean[r][c];
        
        int count = 0;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    dfs(grid, visited, i, j);
                    count++;
                }
            }
        }
        
        return count;
    }
    
    public void dfs(char[][] grid, boolean[][] visited, int i, int j) {
        visited[i][j] = true;
        int[] dx = new int[] {0, 0, 1, -1};
        int[] dy = new int[] {1, -1, 0, 0};
        
        for (int k = 0; k < 4; ++k) {
            int x = i + dx[k];
            int y = j + dy[k];
            
            if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length && grid[x][y] == '1' && !visited[x][y]) {
                dfs(grid, visited, x, y);
            }
        }
    }
}