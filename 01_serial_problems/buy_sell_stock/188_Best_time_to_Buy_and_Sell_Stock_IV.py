'''
188. Best Time to Buy and Sell Stock IV
Hard

3286

149

Add to List

Share
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k==0 or len(prices)<=1:
            return 0
        
        
        ## easy to use k as notation...
        K = k
        T = len(prices)
        ## dp[t][k][0] := on day t, complete k transactions, holding 0 shares; max profit
        ## dp[t][k][1] := on day t, complete k transactions, holding 1 shares; max profit
        
        
        dp = [ [ [0,0] for _ in range(K+1)] for _ in range(T)]
        dp[0][0][1] = -prices[0]
        
        
        for k in range(1,K+1):
            
            for t in range(2*k-1):
                if t>= T:
                    break
                    
                dp[t][k][0] = -float('inf')
            
            for t in range(2*k):
                if t>= T:
                    break
                    
                dp[t][k][1] = -float('inf')
        
        for t in range(1, T):
            for k in range(1,K+1):
                dp[t][k][0] = max(dp[t-1][k][0], dp[t-1][k-1][1] + prices[t])
                
                
            for k in range(0,K+1):
                
                dp[t][k][1] = max(dp[t-1][k][1], dp[t-1][k][0] - prices[t])

        res = max([dp[T-1][k][0] for k in range(K+1)])
        return res