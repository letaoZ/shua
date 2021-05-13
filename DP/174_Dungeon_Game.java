class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length;
        int n = dungeon[0].length;
        
        int[][] dp = new int[m][n];
        dp[m-1][n-1] = dungeon[m-1][n-1] > 0 ? 1 : 1 - dungeon[m-1][n-1];
        for (int i = m - 2; i >= 0; --i) {
            dp[i][n-1] = setDp(dp[i+1][n-1], dungeon[i][n-1]);
        }
        
        for (int j = n - 2; j >= 0; --j) {
            dp[m-1][j] = setDp(dp[m-1][j+1], dungeon[m-1][j]);
            
        }
        
        for (int i = m - 2; i >= 0; --i) {
            for (int j = n - 2; j >= 0; --j) {
                int right = setDp(dp[i][j+1], dungeon[i][j]);
                int bottom = setDp(dp[i+1][j], dungeon[i][j]);
                dp[i][j] = Math.min(right, bottom);
            }
        }
        
        return dp[0][0];
    }
    
    private int setDp(int a, int b) {
        return b < 0 ? a - b : (a - b <= 1 ? 1 : a - b);
    }
}