'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''


class Solution:
    def climbStairs0(self, n: int) -> int:
        
        
        ## s(N) = s(N-1) + S(N-2)
        ## dp[i] := reaching steps i, number of ways      
        
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for k in range(2, n+1):
            dp[k] = dp[k-1] + dp[k-2]
        
        return dp[-1]
        
    def climbStairs(self, n: int) -> int:
        
        
        ## s(N) = s(N-1) + S(N-2)
        ## dp[i] := reaching steps i, number of ways       
        ## only need previous two values and no need for extra storage
        n0, n1 = 1, 1
        
        while n>=2:
            n0 = n0 + n1
            n0, n1 = n1, n0
            n -= 1
        
        return n1