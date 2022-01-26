'''
983. Minimum Cost For Tickets
Medium

4020

69

Add to List

Share
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
 

Constraints:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000

'''

class Solution:
    
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        ### dp[k][i] := traveling arrived on day k, min cost, if i
        ## i = 0,1,2 costs[i], bought tickets with cost[i]; i = 3 didn't buy tickets
        from sortedcontainers import SortedSet
        days = list(SortedSet(days))
        
        cost = 0        
        
        i = 0
        past7 = collections.deque()
        past30 = collections.deque()
        
        while i<len(days):
            # print(days[i])
            # print("past 7, ", past7)
            # print("past 30, ", past30)
            d = days[i]
            while past7:
                if past7[0][0] + 7 - 1 < d:
                    past7.popleft()
                else:
                    break
            while past30:
                if past30[0][0] + 30 - 1 < d:
                    past30.popleft()
                else:
                    break
            past7.append( (d, cost+costs[1]))
            past30.append( (d, cost+costs[2]))
            cost = min(cost + costs[0], past7[0][1], past30[0][1])
            # print("cost" , cost)
            i += 1
        return cost
        
    def mincostTickets_mem_N(self, days: List[int], costs: List[int]) -> int:
        ### dp[k][i] := traveling arrived on day k, min cost, if i
        ## i = 0,1,2 costs[i], bought tickets with cost[i]; i = 3 didn't buy tickets
        from sortedcontainers import SortedSet
        days = list(SortedSet(days))
        if len(days) == 1:
            return min(costs)
        

            
        ## dp[i] := min cost to reach day i
        
        days = [_ - days[0]+1 for _ in days]
        
        dp = [float('inf')]*(days[-1]+1)        
        dp[0] = 0        
        costs_map = {c:delta for delta,c in zip(costs,[1,7,30])}
        # print(days)
        # print(dp)
        for i in range(1,days[-1]+1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                cur_res = float("inf")
                for k in [1,7,30]:
                    if i-k>0:
                        cur_res = min(dp[i-k]+costs_map[k], cur_res)
                    else:
                        cur_res = min(cur_res, costs_map[k])

                dp[i] = cur_res
                
        ## eg input is [1,300], it means you travel on day 1, then rest; till day 300, you must travel
        return dp[-1]