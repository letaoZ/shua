'''
741. Cherry Pickup
Hard

You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, or
-1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:

Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.
 

Example 1:


Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
Output: 5
Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
Example 2:

Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
Output: 0
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 50
grid[i][j] is -1, 0, or 1.
grid[0][0] != -1
grid[n - 1][n - 1] != -1

'''


## IDEA: need to assume dp[i][j] as STARTING from I,J, max result we get!!!
class Solution:
    
    def cherryPickup1(self, grid: List[List[int]]) -> int:
        
        ## 1--> n-1
        ## -1 -->0
        ## dp[i][j] max cherry collected when starting i,j
        SZ = len(grid)
        dp = [[ [-2]*(SZ) for _ in range(SZ)] for _ in range(SZ)]
        
        def searching(g,x1,y1,x2):
            y2 = x1+y1 - x2
            
            if x1>=SZ or x2 >= SZ or y1 >= SZ or y2 >= SZ or x1<0 or x2<0 or y1<0 or y2<0:
                return -1
            
            
            if dp[x1][y1][x2] !=-2:
                return dp[x1][y1][x2]
            
            if g[x1][y1] == -1 or g[x2][y2] == -1:
                dp[x1][y1][x2] = -1
                return -1
            
            if x1==x2==y1==y2 == 0:
                return g[x1][y1]
            if x1 == x2 and y1==y2:
                delta = g[x1][y1] 
            else:
                delta =  g[x1][y1] + g[x2][y2]
                
            addition = max(
                searching(g,x1-1,y1,x2-1), searching(g,x1-1,y1,x2), 
                searching(g,x1,y1-1,x2-1), searching(g,x1,y1-1,x2))
            
            if addition == -1:
                dp[x1][y1][x2] = -1 
                return -1
            
            
            dp[x1][y1][x2] = delta + addition
            return dp[x1][y1][x2]
        
        res = searching(grid,SZ-1,SZ-1,SZ-1)
        return res if res>=0 else 0        
            
                            
        
    def cherryPickup_dp_4dim_needto_reduce_dimension(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == -1 or grid[-1][-1]==-1:
            return 0
        
        ## 1--> n-1
        ## -1 -->0
        ## dp[i][j] max cherry collected when starting i,j
        SZ = len(grid)
        dp = [[[ [-2]*(SZ) for _ in range(SZ)] for _ in range(SZ)] for _ in range(SZ)]
        
        def searching(g,x1,y1,x2,y2):
            if x1>=SZ or x2 >= SZ or y1 >= SZ or y2 >= SZ or x1<0 or x2<0 or y1<0 or y2<0:
                return -1
            
            
            if dp[x1][y1][x2][y2]!=-2:
                return dp[x1][y1][x2][y2]
            
            if g[x1][y1] == -1 or g[x2][y2] == -1:
                dp[x1][y1][x2][y2] = -1
                return -1
            if x1==x2==y1==y2 == 0:
                return g[x1][y1]
            if x1 == x2 and y1==y2:
                delta = g[x1][y1] 
            else:
                delta =  g[x1][y1] + g[x2][y2]
                
            addition = max(
                searching(g,x1-1,y1,x2-1,y2), searching(g,x1-1,y1,x2,y2-1), 
                searching(g,x1,y1-1,x2-1,y2), searching(g,x1,y1-1,x2,y2-1))
            
            if addition == -1:
                dp[x1][y1][x2][y2] = -1
                return -1
            
            
            dp[x1][y1][x2][y2] = delta + addition
            return dp[x1][y1][x2][y2]
        
        res = searching(grid,SZ-1,SZ-1,SZ-1,SZ-1)
        return res if res>=0 else 0        
            
                            
        