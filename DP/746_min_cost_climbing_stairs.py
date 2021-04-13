'''
746. Min Cost Climbing Stairs
Easy

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999


'''



class Solution:
    def minCostClimbingStairs_dp_memo(self, cost) -> int:
        
        ## time O(N), space O(N)
        def searching(step, cost, dp):

            if step<0:
                return 0

            if dp[step]<float('inf'):
                return dp[step]


            dp[step] = min(searching(step-1,cost,dp),searching(step-2,cost,dp)) + cost[step]

            return dp[step]
        sz = len(cost)
        if sz<=2:
            return min(cost) if sz!=0 else 0


        dp = [float('inf') for _ in range(sz)]
        dp[0] = cost[0]
        dp[1] = cost[1]


        searching(sz-1,cost,dp)
        return min(dp[-2:])

    def minCostClimbingStairs_memo(self, cost) -> int:
    

        ## time O(N), space O(N)
        sz = len(cost)
        if sz<=2:
            return min(cost) if sz!=0 else 0


        dp = [float('inf') for _ in range(sz)]
        dp[0] = cost[0]
        dp[1] = cost[1]

        
        for L in range(3,sz+1):

            dp[L-1] = min(dp[L-2],dp[L-3]) + cost[L-1]

        return min(dp[-2:])



    def minCostClimbingStairs_memo3(self, cost) -> int:
    

        ## Time O(N), space const
        sz = len(cost)
        dp = [cost[0],cost[1],float('inf')]
        for L in range(3,sz+1):
            dp[2] = min(dp[1],dp[0]) + cost[L-1]
            dp[0] = dp[1]
            dp[1] = dp[2]
        return min(dp)


    def minCostClimbingStairs_modify_cost(self, cost) -> int:
        ## time O(N), no extra space cost
        sz = len(cost)
        for L in range(3,sz+1):
            cost[L-1] = min(cost[L-2],cost[L-3]) + cost[L-1]

        return min(cost[-2:])

        

cost = [1,90,20]
cost = [1,1,4,1]
# cost = [1,1]
# cost = [1]
# cost = [1,90,90,90]


tester = Solution()
tester.minCostClimbingStairs_memo_save(cost)