/*
 * The initial value need to be set correctly considering the obstacle position
 */

class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid == null || obstacleGrid.length == 0 || obstacleGrid[0].length == 0) return 0;
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[] arr = new int[n];
        arr[0] = 1;
        for (int i = 0; i < m; ++i) {
            arr[0] = arr[0] & (1 ^ obstacleGrid[i][0]);
            for (int j = 1; j < n; ++j) {
                arr[j] = obstacleGrid[i][j] == 1 ? 0 : arr[j] + arr[j-1];
            }
        }
        
        return arr[n-1];
    }
}