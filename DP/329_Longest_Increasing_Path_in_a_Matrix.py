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
        
        ## res[i][j] := longest path starting at i,j
        res = [[0]*n for _ in range(m)]
        
        ## store max len so far
        res0 = [1]
        
        def dfs(i,j):
            
            if not (0<=i<m and 0<=j<n):
                return 0
            if res[i][j]:
                return res[i][j]
            
            res[i][j] = 1
            
            tmp = 0
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                x,y = i+di, j+dj
                if (0<=x<m and 0<=y<n and matrix[i][j]<matrix[x][y]):                              
                    tmp = max(tmp, dfs(x,y) )
                    
            res[i][j] += tmp
            res0[0] = max(res0[0], res[i][j])
            return res[i][j]
        
        for i in range(m):
            for j in range(n):
                if not res[i][j]:
                    dfs(i,j)
        return res0[0]