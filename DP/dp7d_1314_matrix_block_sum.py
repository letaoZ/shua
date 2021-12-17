'''
1314. Matrix Block Sum
Medium

1417

230

Add to List

Share
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100
'''

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(mat)
        if m==0:
            return mat
        
        n = len(mat[0])
        if n == 0:
            return mat
        
        ## dp[i][j] = sum of all elements of submat mat[:i][:j]
        dp = [[0]*(n+1) for _ in range(m+1)]
        
    
        for i in range(1,m+1):
            for j in range(1, n+1 ):
                dp[i][j] = dp[i-1][j] + (dp[i][j-1] - dp[i-1][j-1]) + mat[i-1][j-1]
       
        ans = [[0]*n for _ in range(m)]
        for i in range(0,m):
            for j in range(0, n ):
                ans[i][j]  = ( 
                    dp[min(m,i+k+1)][min(n,j+k+1)] -
                    (dp[max(0,i-k) ][min(n,j+k+1)] - dp[max(0,i-k)][max(0,j-k)]) -
                    dp[min(m,i+k+1)][max(0,j-k)] )
                
        return ans