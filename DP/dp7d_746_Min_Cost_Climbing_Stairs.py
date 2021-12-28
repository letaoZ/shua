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
    
    def minCostClimbingStairs_Mem_N(self, cost: List[int]) -> int:
        
        ## dp[i]:=min cost to arrive cost[i]
        ## NOTE: we will return min(dp[-1],dp[-2]) 
        ## because we can reach the top either jumping from the last or the 2nd from the last position
        
        N = len(cost)
        dp = [float('inf')]*(N)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,N):
            dp[i] = min(dp[i-1],dp[i-2])  + cost[i]
            
        return min(dp[-2],dp[-1])
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        ## dp[i]:=min cost to arrive cost[i]
        ## NOTE: we will return min(dp[-1],dp[-2]) 
        ## because we can reach the top either jumping from the last or the 2nd from the last position
        
        
        dp0 = cost[0]
        dp1 = cost[1]
        for i in range(2,len(cost)):
            dp_new = min(dp0,dp1)  + cost[i]
            dp0, dp1 = dp1, dp_new
        return min(dp0, dp1)