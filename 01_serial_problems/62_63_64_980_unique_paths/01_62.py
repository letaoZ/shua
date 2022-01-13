'''
62. Unique Paths
Medium
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.

'''



class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:

        ## dp[-1][*] and dp[*][-1] can be accessed as "0"
        dp =  [0]*(n+1) 
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                dp[j] = dp[j] + dp[j-1]
        return dp[n-1]
        
        
    def uniquePaths_bottomup(self, m: int, n: int) -> int:
        
        
        dp =[ [0]*(n+1) for _ in range(m+1)]
        
        ## dp[i][j] num of ways to reach (i,j)
        ## add cushion row and column
        ## dp[-1][*] and dp[*][-1] can be accessed as "0"
        dp[0][0] = 1
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                dp[i][j] += dp[i-1][j] + dp[i][j-1] ## since dp[i][j] will be updated once, we can use "+" to avoid dp[0][0] assignment issue
        return dp[m-1][n-1]
    def uniquePaths_topdown(self, m: int, n: int) -> int:


        ## method 1:
        ## dp
        ## time = O(MN)
        ## space = O(MN)
        dp = [[0]*n for _ in range(m)]

        for j in range(n):
            dp[-1][j] = 1
        for i in range(m):
            dp[i][-1] = 1
        def searching(i,j,m,n,dp):
            if dp[i][j] > 0: 
                return dp[i][j]

            ## dp[i][j] = dp[i+1][j] + dp[i][j+1]
            dp[i][j] = searching(i+1,j,m,n,dp) + searching(i,j+1,m,n,dp)

            return dp[i][j]
        
        return searching(0,0,m,n,dp)


    def uniquePaths_math(self, m: int, n: int) -> int:

        ## metod 2:
        ## all paths consist of: 
        ## M = m-1 many going downs, N = n-1 many going rights
        ## M + N choose M
        ## i.e. there are totally M+N spaces, M of them are filled with downs
        ## time = O(min(m,n))
        def math_choose(a,b): ## a >= b
            if a<=1 or b<=1: return 1

            prod =1
            for k in range(b):
                prod *= (a-k)/(k+1)
            return int(prod)
        return math_choose(m-1+n-1,min(m-1,n-1))



m = 7
n = 3

solu = Solution()
solu.uniquePaths_dp(m,n),solu.uniquePaths_math(m,n)
