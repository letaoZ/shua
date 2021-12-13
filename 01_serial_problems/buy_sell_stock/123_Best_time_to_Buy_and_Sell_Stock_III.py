class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## dp[t][k][0] := on day t, completed k transactions, and hold 0 stocks; max profit you get
        ## dp[t][k][1] := on day t, completed k transactions, and hold 1 stocks; max profit you get
        
        dp = [ [ [0]*2 for _ in range(2+1)] for _ in range(len(prices)) ]
        
        dp[0][0][1] = -prices[0]
        
        ## values cannot be achieved
        ## you need at least 4 days to compete 2 transactions andhold 0
        ## you also need at least 5 days to compete 2 transactions and hold 1
        for k in range(1,3):
            for i in range(2*k):
                if i>= len(prices):
                    break
                dp[i][k][0] = -float('inf')
            for i in range(2*k+1):
                if i>= len(prices):
                    break
                dp[i][k][1] = -float('inf')
            
        
        '''
        ????
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
'''
        
        
        for t in range(1,len(prices)):
            dp[t][0][0] = 0
            bound_k = 2
            for k in range(1,bound_k + 1):    
                #
                dp[t][k][0] = max(dp[t-1][k][0], # no action
                               (dp[t-1][k-1][1] + prices[t]), 
                                  # completed k-1 transactions on or before t-1; and complete the kth on day t
                             )
            for k in range(0,bound_k + 1):    
                dp[t][k][1] = max(dp[t-1][k][1], # no action
                              (dp[t-1][k][0] - prices[t]), # buy a share on day t
                             )
                
#             print(t)
#             print(dp[t])
                
        res = dp[-1][2][0]
        res = max([dp[-1][k][0] for k in range(3)])
        return res