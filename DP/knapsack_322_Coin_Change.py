'''
322. Coin Change
Medium

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 104
'''


class Solution:
    def coinChange_slow(self, coins: List[int], amount: int) -> int:
        ## for each amount/weight w, find the fewest possible numb of coins
        
        
        ## dp[i][w] : to reach amount w and using first i coins, the min num of coins used
        dp = [ [float('inf')]*(amount+1) for _ in range(len(coins))]
        
        
        for i in range(len(coins)):
            dp[i][0] = 0
        
        
        
        for i in range(len(coins)):
            for w in range(1,amount+1):
                for coin in coins[:i+1]:
                    nc = w//coin + 1
                    for k in range(1,nc):
                        
                        dp[i][w] = min(dp[i][w- k*coin] + k, dp[i][w])
                        
        if dp[-1][-1] < float('inf'):
            res = dp[-1][-1]
        else:
            res = -1
        return res

    
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## for each amount/weight w, find the fewest possible numb of coins
        
        ## UNBOUNDED knapsack problem
        
        ## precheck
        coins = list(set(coins))
        
        ## check amount
        if amount <min(coins) and amount!=0:
            return -1
        
        ## dp[w] : to reach amount w min coins used
        dp = [float('inf')]*(amount+1)
        dp[0] = 0        
        
        for i in range(len(coins)):
            coin = coins[i]
            for w in range(coin,amount+1):
                        
                dp[w] = min(dp[w- coin] + 1, dp[w])


        return dp[-1] if dp[-1]<float('inf') else -1