'''
576. Out of Boundary Paths
Medium

1374

180

Add to List

Share
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
 

Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
'''

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # print(m,n,N,i,j)
        if N<=0:
            return 0
        ## dp[a][b] := num of ways out starting at a,b
        ## dp[a][b] = dp[a-1][b]+dp[a][b-1] + dp[a][b+1] + dp[a+1][b]
        M = int(1e9 + 7)
        dp = [[[-1]*n for _ in range(m)] for _ in range(N+1)]
        I,J = i,j

        def searching(x,y,steps_left):
            # print(f"searching: {x} {y} {steps_left}")
            if steps_left <= 0 or (
                x+steps_left<m and y+steps_left<n and x-steps_left>0 and y-steps_left > 0):
                return 0
            if dp[steps_left][x][y] >= 0:
                return dp[steps_left][x][y]
            cur_res=0
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x1, y1 = x+dx, y+dy
                if not (0 <= x1 <m and 0<= y1 <n):
                    cur_res += 1
                    continue
                cur_res += (searching(x1,y1, steps_left-1) % M)
            # print(f"searching: {x} {y} DONE")
            cur_res %= M
            dp[steps_left][x][y] = cur_res 
            return cur_res
        
        res = searching(I,J,N)
        # print(dp)

        return res      