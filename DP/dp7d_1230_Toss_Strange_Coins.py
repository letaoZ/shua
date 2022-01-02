'''
1230. Toss Strange Coins
Medium

194

15

Add to List

Share
You have some coins.  The i-th coin has a probability prob[i] of facing heads when tossed.

Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.

 

Example 1:

Input: prob = [0.4], target = 1
Output: 0.40000
Example 2:

Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
Output: 0.03125
 

Constraints:

1 <= prob.length <= 1000
0 <= prob[i] <= 1
0 <= target <= prob.length
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
'''

class Solution:
    def probabilityOfHeads_mem_mn(self, prob: List[float], target: int) -> float:
        ## dp[n][l] := using first n coins, get l heads probability
        ## dp[n][l] = dp[n-1][l]*(1-prob[n])  + dp[n-1][l-1]*prob[n] ## conditional prob
        
        dp = [ [0]*(target+1) for _ in range(len(prob)+1)]
        ## 0 coins will get 0 head with probability 1
        ## n coin will get l head with prob 0 if l>=n
        dp[0][0] = 1 
        for n in range(1,len(prob)+1):
            dp[n][0] = dp[n-1][0]*(1-prob[n-1])
            for l in range(1, min(target+1,n+1) ):
                dp[n][l] = dp[n-1][l]*(1-prob[n-1])  + dp[n-1][l-1]*prob[n-1]
        # print(dp)
        return dp[-1][-1]
    
    def probabilityOfHeads_mem_reduce(self, prob: List[float], target: int) -> float:
        
        ## mem reduce N
        ## dp[n][l] := using first n coins, get l heads probability
        ## dp[n][l] = dp[n-1][l]*(1-prob[n])  + dp[n-1][l-1]*prob[n] ## conditional prob
        
        dp =  [0]*(target+1)
        ## 0 coins will get 0 head with probability 1
        ## n coin will get l head with prob 0 if l>=n
        dp[0] = 1 
        for n in range(1,len(prob)+1):
            for l in range(min(target,n) , 0,-1):
                dp[l] = dp[l]*(1-prob[n-1])  + dp[l-1]*prob[n-1]
            dp[0] = dp[0]*(1-prob[n-1])

        # print(dp)
        return dp[-1]
    
    def probabilityOfHeads_slow_recur(self, prob: List[float], target: int) -> float:
        
        ## slow recursion
        @functools.lru_cache(maxsize=128)
        def searching(i,cur_target,prev_p):
            if len(prob[i:]) == cur_target:
                p = 1
                for k in prob[i:]:
                    p *= k
                return prev_p*p
            elif len(prob[i:]) < cur_target:
                return 0
            
            elif cur_target == 0:
                p = 1
                for k in prob[i:]:
                    p *= (1-k)
                return prev_p*p
            
            a = searching(i+1, cur_target-1, prev_p*(prob[i]))
            b = searching(i+1, cur_target, prev_p*(1-prob[i]))
            return a+b
            
            
        res = searching(0, target, 1)
        return res