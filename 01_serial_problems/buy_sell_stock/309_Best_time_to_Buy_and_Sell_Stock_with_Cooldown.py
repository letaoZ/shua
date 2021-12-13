'''
309. Best Time to Buy and Sell Stock with Cooldown
Medium

4959

170

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 比如说这个问题，每天都有三种「选择」：买入、卖出、无操作，我们用 buy, sell, rest 表示这三种选择。
        # dp[i][k][0 or 1]: on day i (0-- hold nothing, 1--hold stock), and we have traded at most k times: max money we got
        # NOTE: to hold stock 0->1 we spend -price, and to sell stock, we got from 1->0 +price to get the stock
        # 0 <= i <= n - 1, 1 <= k <= K, n 为天数，大 K 为交易数的上限，0 和 1 代表是否持有股票。
        # 此问题共 n × K × 2 种状态，全部穷举就能搞定。
        
        ## k = +infinity with cooldown
        ## on day i
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        
        if len(prices)<=2:
            return max(0,prices[-1] - prices[0])
        N = len(prices)
        dp = [[0,0] for _ in range(N)]
    
        dp[0][1] = -prices[0]
        dp[0][0] = 0
        
    
        for i in range(1,N):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        
        return dp[-1][0]
                