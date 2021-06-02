'''1223. Dice Roll Simulation

A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times. 

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls.

Two sequences are considered different if at least one element differs from each other. Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
Example 2:

Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30
Example 3:

Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181
 

Constraints:

1 <= n <= 5000
rollMax.length == 6
1 <= rollMax[i] <= 15

'''


import collections


class Solution:

    
    def dieSimulator_dfs_topdown_noDP(self, n: int, rollMax: List[int]) -> int:
        M = (10**9 + 7)

        
        ## if rollMax[i]>=n, then you have no actual contraint
        
        constraint_keys = [v for v in rollMax if v>=n]
      
        if len(constraint_keys) == 6:
            return 6**n
        
        

        total = [0]
        

        def searching(prev_num,prev_len, rollMax,rolln, total):
            if rolln==0:
                total[0] += 1
                total[0]%=M
                return
            
            for k in range(6):
                if k!= prev_num:
                    if rollMax[k]>0:
                        searching(k,1, rollMax,rolln-1, total)
                        
                else:
                    if prev_len < rollMax[k]:
                        searching(k,prev_len+1, rollMax,rolln-1, total)
                        
                    
                    
                    
                    
                    
        searching(-1,1, rollMax, n, total)
        
        print(total)
        return total[0]
                    
            
            
            

    def dieSimulator_dp_tooMuch_memo(self, n: int, rollMax: List[int]) -> int:

        
        M = (10**9 + 7)
        ## if rollMax[i]>=n, then you have no actual contraint
        
        constraint_keys = [v for v in rollMax if v>=n]
        if len(constraint_keys) == 6:
            return (6**n % M)
        
        for i,v in enumerate(rollMax):
            if v>n:
                rollMax[i] = n
        
        ## dp[L][face][faceRep] -- for L rolls, the last roll is face k, repeat faceRep many times
        ## number of different sequence
        dp = [ [ [0]*(max(rollMax)+1) for k in range(6)] for _ in range(n+1)]
        
        for k in range(6):
                
            dp[1][k][1] = 1
            dp[1][k][0] = 5
            
        for L in range(2,n+1):
            for k in range(6):
                
                
                for ek in range(1, rollMax[k]+1):
                    if ek>L: break
                    dp[L][k][ek] = dp[L-1][k][ek-1] 
            
            for k in range(6):
                dp[L][k][0] = sum([sum(dp[L][j][1:])%M for j in range(6) if j!=k])
                dp[L][k][0] %= M
                
        res = 0
        for i in range(6):
            res += sum(dp[n][i][1:])
            res %= (10**9 + 7)
            
        return res
        
        
        

    def dieSimulator_bottomUP_dimReduction(self, n: int, rollMax: List[int]) -> int:

        
        M = (10**9 + 7)
        ## if rollMax[i]>=n, then you have no actual contraint
        constraint_keys = [v for v in rollMax if v>=n]
        if len(constraint_keys) == 6:
            return (6**n % M)
        
        for i,v in enumerate(rollMax):
            if v>n:
                rollMax[i] = n
        
        ## dp[L][face][faceRep] -- for L rolls, the last roll is face k, repeat faceRep many times
        ## number of different sequence
        dp = [ [0]*(max(rollMax)+1) for k in range(6)]
        
        for k in range(6):
                
            dp[k][1] = 1
            dp[k][0] = 5
        
        for L in range(2,n+1):
            for k in range(6):
                EK = min(L, rollMax[k])
                
                dp[k][1:EK+1] = dp[k][:EK] 
                
            for k in range(6):
                dp[k][0] = sum([sum(dp[j][1:])%M for j in range(6) if j!=k])
                dp[k][0] %= M
                
        res = 0
        for i in range(6):
            res += sum(dp[i][1:])
            res %= (10**9 + 7)
            
        return res
    
    

    
    ### wrong!! but with possibility of improvement
    ###############################################3
    def dieSimulator_bottomUP_dimReduction_more(self, n: int, rollMax: List[int]) -> int:

        
        M = (10**9 + 7)
        ## if rollMax[i]>=n, then you have no actual contraint
        constraint_keys = [v for v in rollMax if v>=n]
        if len(constraint_keys) == 6:
            return (6**n % M)
        
        for i,v in enumerate(rollMax):
            if v>n:
                rollMax[i] = n
        
        ## dp[L][face][faceRep] -- for L rolls, the last roll is face k, repeat faceRep many times
        ## number of different sequence
        dp = [ [0]*(max(rollMax)+1) for k in range(6)]
        dp1 = [ [0]*(1+1) for k in range(6)]
        
        for k in range(6):
                
            dp[k][1] = 1
            dp[k][0] = 5
           
            dp1[k][1] = 1
            dp1[k][0] = 5
        
        for L in range(2,n+1):
            for k in range(6):
                EK = min(L, rollMax[k])
                
                dp[k][1:EK+1] = dp[k][:EK] 
                 ## here dp1 has no control of EK!
                dp1[k][1] = sum(dp1[k])
                
            for k in range(6):
                dp[k][0] = sum([sum(dp[j][1:])%M for j in range(6) if j!=k])
                dp[k][0] %= M
                dp1[k][0] = sum([dp1[j][1] for j in range(6) if j!=k])
                dp1[k][0] %= M
        res = 0
        res1 = 0
        for i in range(6):
            res += sum(dp[i][1:])
            res %= (10**9 + 7)
            res1 += dp1[i][1]
        print(res1)
        return res
    
