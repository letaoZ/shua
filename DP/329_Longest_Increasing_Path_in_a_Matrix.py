'''
329. Longest Increasing Path in a Matrix
Hard

4642

81

Add to List

Share
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
'''

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ## dfs longest increasing so far
        
        m, n = len(matrix), len(matrix[0])
        
        
        ## 
        ## starting at (i,j), the longest increasing sequence
        ##
        res = [1]
        dp = [[0]*n for _ in range(m)]
        def dfs(i,j):
            if not (0 <= i < m and 0 <= j < n):
                return 0
            
            if dp[i][j] > 0:
                return dp[i][j]
            dp[i][j] = 1 
            for dx, dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                x, y =i + dx, j + dy
                if not (0 <= x < m and 0 <= y < n):
                    continue
                
                if matrix[i][j] < matrix[x][y]: ## the path starting at x,y can be extended to starting at i,j
                    dp[i][j] = max(dp[i][j], dfs(x,y)+1)
        
            res[0] = max(res[0], dp[i][j])
            return dp[i][j] 

        for i in range(m):
            for j in range(n):
                if dp[i][j] != 0:
                    continue
                dfs(i,j)
        return res[0]