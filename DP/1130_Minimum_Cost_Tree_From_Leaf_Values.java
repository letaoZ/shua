/**
 * Need to reason about the bottom up approach other than memoization. Two dp can also be merged into one function.
 */

class Solution {
    public int mctFromLeafValues(int[] arr) {
        int[][] memo = new int[arr.length][arr.length];
        int[][] maxmemo = new int[arr.length][arr.length];
        dp2(0, arr.length - 1, arr, maxmemo);
        return dp(0, arr.length - 1, arr, memo, maxmemo);
    }
    
    public int dp(int i, int j, int[] arr, int[][] memo, int[][] maxmemo) {
        if (memo[i][j] != 0) return memo[i][j];
        
        if (i == j) {
            memo[i][j] = 0;
            return memo[i][j];
        }
        
        if (i == j - 1) {
            memo[i][j] = arr[i] * arr[j];
            return memo[i][j];
        }
        
        int value = Integer.MAX_VALUE;
        for (int k = i; k < j; ++k) {
            int l = dp(i, k, arr, memo, maxmemo);
            int r = dp(k+1, j, arr, memo, maxmemo);
            value = Math.min(value, maxmemo[i][k] * maxmemo[k+1][j] + l + r);
        }
        
        memo [i][j] = value;
        return memo[i][j];
    }
    
    public int dp2(int i, int j, int[] arr, int[][] maxmemo) {
        if (maxmemo[i][j] != 0) {
            return maxmemo[i][j];
        }
        
        if (i == j) {
            maxmemo[i][j] = arr[i];
            return maxmemo[i][j];
        }
        
        for (int k = i; k < j; ++k) {
            maxmemo[i][j] = Math.max(dp2(i, k, arr, maxmemo), dp2(k + 1, j, arr, maxmemo));
        }
        
        
        
        return maxmemo[i][j];
    }


    /**
     * The buggy DP2. This cannot guarantee filling all the (i, j) combos. For example [6, 2, 4],
     * dp[1, 2] will not be filled, which should be 4.
     */
    public buggy_dp2_impl(int i, int j, int[] arr, int[][] maxmemo) {
        if (maxmemo[i][j] != 0) {
            return maxmemo[i][j];
        }
        
        if (i == j) {
            maxmemo[i][j] = arr[i];
            return maxmemo[i][j];
        }
        
        int k = i + (j - i) / 2;
        maxmemo[i][j] = Math.max(dp2(i, k, arr, maxmemo), dp2(k + 1, j, arr, maxmemo));
        
        return maxmemo[i][j];
    }
}