'''
562. Longest Line of Consecutive One in Matrix
Medium

642

95

Add to List

Share
Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, or anti-diagonal.

 

Example 1:


Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3
Example 2:


Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
'''

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        ## we follow the order from the upper left to the lower right
        ## every point has direction from  top left(diag),top(vertical),top right(anti diag), left (horiz), use 0-3 to denote
        
        m, n = len(mat), len(mat[0])
        
        dp = [ [ [0]*4 for _ in range(n)] for _ in range(m)] 
        
        ## dp[i][j][*] = 0 if mat[i][j] = 0
        #  dp[i][j][0] = dp[i-1][j-1][0]  + 1; dp[i][j][1] = dp[i-1][j][1]  + 1; dp[i-1][j+1][2] = dp[i-1][j][2]  + 1;dp[i][j][3] = dp[i][j-1][3]  + 1;
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                
                dp[i][j][0] = int(i-1>=0 and j-1>=0)*dp[i-1][j-1][0]  + 1
                dp[i][j][1] = int(i-1>=0)*dp[i-1][j][1]  + 1
                # print(i,j)
                # print(dp[i][j+1])
                dp[i][j][2] = dp[i-1][j+1][2] + 1 if (i-1>=0 and j+1<n) else 1
                dp[i][j][3] = int(j-1>=0)*dp[i][j-1][3]  + 1
                res = max(res, max(dp[i][j]))
                
        return res
                
