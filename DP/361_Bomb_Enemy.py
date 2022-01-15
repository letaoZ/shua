'''
361. Bomb Enemy
Medium

722

90

Add to List

Share
Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.

The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.

 

Example 1:


Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3
Example 2:


Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 'W', 'E', or '0'.

'''
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        ## rowkill[i][j] := max enemy killed in the row of i, at position i,j
        ## colkill[i][j] := max enemy killed in the col of j, at position i,j
        
        ## traverse row top to bottom and then bottom to top
        ## traverse cols left to right and right to left
        
        m, n = len(grid), len(grid[0])
        rowkill =[ [0]*n for _ in range(m)]
        colkill =[ [0]*n for _ in range(m)]
        res = 0
        
        ## compute top of each elt max enemy killed
        ## we don't include the spot there
        for j in range(0,n):
            for i in range(1,m):
                if grid[i][j] == 'W':
                    continue

                colkill[i][j] = colkill[i-1][j] + int(grid[i-1][j] == 'E')

        for j in range(0,n):
            cnt = 0
            for i in range(m-2,-1,-1):
                if grid[i][j] == 'W':
                    cnt = 0
                    continue
                cnt +=  int(grid[i+1][j] == 'E')
                colkill[i][j] +=cnt

        ## compute left of each elt max enemy killed
        ## we don't include the spot there
        for i in range(m):
            for j in range(1,n):
                if grid[i][j] == 'W':
                    continue
                    
                rowkill[i][j] = rowkill[i][j-1] + int(grid[i][j-1] == 'E')
                
        for i in range(m):
            cnt=0
            for j in range(n-2,-1,-1):
                if grid[i][j] == 'W':
                    cnt = 0
                    continue
                cnt += int(grid[i][j+1] == 'E')
                rowkill[i][j] +=  cnt
        
        # print(rowkill)
        # print(colkill)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res,rowkill[i][j] + colkill[i][j])
                

        return res
        