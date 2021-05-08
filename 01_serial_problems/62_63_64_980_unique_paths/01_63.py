'''
63. Unique Paths II
Medium

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
    ## time = O(mn), space = O(mn)
    def uniquePathsWithObstacles_dp_recurr(self, obstacleGrid: List[List[int]]) -> int:
        def searching(i,j,m,n,obstacleGrid):
            if i>=m: 
                return 0
            if j>=n: 
                return 0
            if obstacleGrid[i][j]>0:
                return 0

            if dp[i][j] > 0:
                return dp[i][j]


            dp[i][j] = searching(i+1,j,m,n,obstacleGrid)\
                + searching(i,j+1,m,n,obstacleGrid)
            return dp[i][j]


        # obstacleGrid = [[0,1],[0,0],[0,0] ]
        # obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]

        m = len(obstacleGrid)
        if m==0:
            return 0
        
        n = len(obstacleGrid[0])
        if n==0:
            return 0

        if obstacleGrid[-1][-1] ==0 or obstacleGrid[0][0]==1: 
            return 0
            
        dp = [ [0]*n for _ in range(m)]
        dp[-1][-1] = 1

        return searching(0,0,m,n,obstacleGrid)


    def uniquePathsWithObstacles_dp_no_recurr(self, obstacleGrid):

        m = len(obstacleGrid)
        if m==0:
            return 0
        
        n = len(obstacleGrid[0])
        if n==0:
            return 0

 

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 0:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.            
        return obstacleGrid[-1][-1]
    
    


        