'''
63. Unique Paths II
Medium

3940

347

Add to List

Share
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        ## dp[i][j] := num of ways to reach (i,j)
        ## if obstacleGrid[i][j] == 1, dp[i][j] = 0
        if obstacleGrid[0][0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = 1
        for i in range(m):
            if i>0:
                dp[i][0] = dp[i-1][0]*( 1 - obstacleGrid[i][0] )

            for j in range(1,n):
                dp[i][j] = ( 1 - obstacleGrid[i][j] )*(dp[i-1][j] + dp[i][j-1])

        return dp[m-1][n-1]