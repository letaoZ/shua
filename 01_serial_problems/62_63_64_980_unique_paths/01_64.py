
'''
64. Minimum Path Sum
Medium

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


    
    def minPathSum_bottomUp(self, grid: List[List[int]]) -> int:
        
        
        ## dp to keep track of starting from i,j; min value we get
        ## add cushion as well
        
        M, N = len(grid), len(grid[0])
        
        dp = [ [float('inf')]*(N) for _ in range(M)]

        dp[M-1][N-1] = grid[M-1][N-1]
        def searching(grid,i,j,dp):
            if i>=M or j>=N:
                return float('inf')
            
                
            if dp[i][j]<float('inf'):
                return dp[i][j]
            tmp = min(searching(grid, i,j+1,dp),searching(grid,i+1,j,dp))
            if tmp == float('inf'):
                return tmp
            
            dp[i][j] = grid[i][j] + tmp
            return dp[i][j]
            
        res = searching(grid,0,0,dp)
        return res


    def minPathSum_topdown_2d(self, grid: List[List[int]]) -> int:

        
        M, N = len(grid), len(grid[0])
        
        dp = [ [float('inf')]*(N+1) for _ in range(M+1)]

        
        dp[M][N-1] = dp[M-1][N] = 0
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                
                ## add cushion for the i=M-1, j = N-1
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
        
        return dp[0][0]
 
    def minPathSum_topdown_1d(self, grid: List[List[int]]) -> int:

        
        M, N = len(grid), len(grid[0])
        
        dp =[float('inf')]*(N+1)

        ## make sure that you reduce ALL parts from each row label
        ## starting at M
        ## dp[M][N-1]
        dp[N-1] = 0
        for i in range(M-1,-1,-1):
            # dptmp = [tt for tt in dp]
            for j in range(N-1,-1,-1):
                
                ## add cushion for the i=M-1, j = N-1
                ## observe that tmp is not required
                # dp[j] = min(dptmp[j], dp[j+1]) + grid[i][j]
                dp[j] = min(dp[j], dp[j+1]) + grid[i][j]

        return dp[0]
    
    
    
    def minPathSum_noExtra_Space(self, grid: List[List[int]]) -> int:
        ## no extra space by modifying original grid
        
        M, N = len(grid), len(grid[0])
        
        
        
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                if i+1<M and j+1<N:
                    grid[i][j] += min(grid[i+1][j],grid[i][j+1]) 
                elif i+1<M:
                    grid[i][j] += grid[i+1][j]
                    
                elif j+1<N:
                    grid[i][j] += grid[i][j+1]
                    

        return grid[0][0]
    
  
    def minPathSum_ExtraSpace_Cushion_grid(self, grid: List[List[int]]) -> int:
        ## M + M space by modifying original grid
        #
        M, N = len(grid), len(grid[0])
        grid += ([[float('inf')]*N])

        for i in range(M+1):
            grid[i].append(float('inf'))
            
        grid[M][N-1] = grid[M-1][N] = 0
        
        
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                grid[i][j] += min(grid[i+1][j],grid[i][j+1]) 

                    

        return grid[0][0]      
        

   
    