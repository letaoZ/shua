'''1140. Stone Game II
Medium


Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104
 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 104
'''

import collections
List = list
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        ## compute alice - bob
        ## then we know alice + bob = sum(piles), to compute alice
        ## time = SZ^3
        
        SZ = len(piles)
        
        ## dp[M][i]: taking at most 2M piles, starting from ith pile, max score get
        dp = [[-float('inf')]*(SZ*2) for _ in range(SZ)]

        ## partial sum i to the end
        psum = [0]*(SZ+1)
        for i in range(SZ-1,-1,-1):
            psum[i] = psum[i+1] + piles[i]
            
            
        def searching(piles,prev_M,i): ## starting from i tile the end
            boundM = 2*prev_M
            if i>=SZ:
                return 0
            if (i+boundM-1>=SZ-1): 
                return psum[i]
            if dp[prev_M][i] > -float('inf'):
                return dp[prev_M][i]
            
            res = -float('inf')
            for X in range(1,boundM+1):
                res = max(res, 
                          sum(piles[i:i+X]) - 
                          searching(piles,max(X,prev_M), i+X)
                         )
            dp[prev_M][i] = res
                
            return res
        
        
        diff = searching(piles, 1, 0)
        alice = (diff+sum(piles))//2
        
        return alice
   
        
    def stoneGameII_dp_noMem(self, piles: List[int]) -> int:

        ## compute alice - bob
        ## then we know alice + bob = sum(piles), to compute alice
        
        SZ = len(piles)


        def searching(piles,prev_M,i): ## starting from i tile the end
            boundM = 2*prev_M
            if i>=SZ:
                return 0
            if (i+boundM-1>=SZ-1): 
                return sum(piles[i:])
            res = -float('inf')
            for X in range(1,boundM+1):
                if i+X >=SZ-1:
                    break
                res = max(res, 
                          sum(piles[i:i+X]) - 
                          searching(piles,max(X,prev_M), i+X)
                         )
                
            return res
        
        
        diff = searching(piles, 1, 0)
        alice = (diff+sum(piles))//2
        
        return alice
                
                
            