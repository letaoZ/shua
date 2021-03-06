'''
64. Minimum Path Sum
Medium

6246

89

Add to List

Share
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100


'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        ## dp[i][j] min sum to reach position i,j
        m, n = len(grid), len(grid[0])
        
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        dp[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                dp[i][j] = min(dp[i][j],  ## to handle index 0,0
                               min(dp[i-1][j],dp[i][j-1]) + grid[i][j])
                
        return dp[m-1][n-1]

    def minPathSum_mem_reduce(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])
        
        ## dp[i][j] := min sum to reach grid[i][j]
        #  dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        #  we can add an extra column and row of value inf to handle out of bound index
        
        dp = [float('inf')]*(n+1) 
        dp[0] = 0
        for i in range(m):
            for j in range(n):
                dp[j] = min(dp[j],dp[j-1]) + grid[i][j]
        return dp[n-1]
