'''
221. Maximal Square
Medium

6299

135

Add to List

Share
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
'''

class Solution:
    def maximalSquare_2d(self, matrix: List[List[str]]) -> int:
        print("2d")
        ## dp[i][j] a square shape's lower right corner is (i,j), max square number
        m, n = len(matrix), len(matrix[0])
        dp = [[0]* (n+1) for _ in range(m+1)]
        res = 0
        for i in range(m):
            # print(f"i: ",i)
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                prev_sq = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) ## 0 - 1 or 0 - 1 is counted as m, n
                dp[i][j] = prev_sq + 1
                res = max(dp[i][j],res)
            # print(dp[i])
            # print()
        return res**2
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ## dp[i][j] a square shape's lower right corner is (i,j), max square number
        m, n = len(matrix), len(matrix[0])
        dp = [0]* (n+1) 
        res = 0
        for i in range(m):
            # print(f"i: {i}")
            tmp = [tt for tt in dp]
            for j in range(n):
                if matrix[i][j] == "0":
                    dp[j] = 0 ## important!
                    continue
                prev_sq = min(tmp[j],tmp[j-1],dp[j-1]) ## 0 - 1 or 0 - 1 is counted as m, n
                dp[j] = prev_sq + 1
                res = max(dp[j],res)
            # print(dp)
            # print()

        return res**2