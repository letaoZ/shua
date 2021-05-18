class Solution {
    public int minScoreTriangulation(int[] values) {
        int[][] memo = new int[values.length][values.length];
        return find(values, 0, values.length - 1, memo);        
    }
    
    public int find(int[] values, int i, int j, int[][] memo) {
        if (i + 1 == j) return 0;
        
        if (memo[i][j] != 0) return memo[i][j];
        
        if (i + 2 == j) {
            memo[i][j] = values[i] * values[i+1] * values[j];
            return memo[i][j];
        }
        
        memo[i][j] = Integer.MAX_VALUE;
        for (int k = i + 1; k < j; ++k) {
            int sum = values[i] * values[k] * values[j];
            sum += find(values, i, k, memo);
            sum += find(values, k, j, memo);
            memo[i][j] = Math.min(memo[i][j], sum);
        }
        
        return memo[i][j];
    }
}