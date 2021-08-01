'''877. Stone Game
Medium

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 

Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
'''









class Solution:
    def stoneGame_tricky(self, piles: List[int]) -> bool:
        ## since sum(piles) is odd and len(piles) is even,
        # sum of even indexed piles != sum of odd indexed piles
        # so one of them is bigger
        # Thus, the first person can always choose the right oddity to win
        return True


    def stoneGame_bottomup_1d_extra_mem(self, piles: List[int]) -> bool:
        sz = len(piles)
        ## dp[j]: at the Lth step piles[j-L, j], max diff between Alice and Bob
        dp = [0]*sz 

        ## initialize l = 1
        for i in range(1,sz):
            dp[i] = piles[i]
        for L in range(2,sz):
            tmp = [kk for kk in dp]
            for j in range(L, sz):
                dp[j] = max(piles[j-L] - tmp[j], piles[j] - tmp[j-1] )               
        return dp[sz-1] > 0


    def stoneGame_bottomup_1d(self, piles: List[int]) -> bool:
        sz = len(piles)
        ## dp[j]: at the Lth step piles[j-L, j], max diff between Alice and Bob
        dp = [0]*sz 

        ## initialize l = 1
        for i in range(1,sz):
            dp[i] = piles[i]
        for L in range(2,sz):
            for j in reversed(range(L, sz) ):
                dp[j] = max(piles[j-L] - dp[j], piles[j] - dp[j-1] )               
        return dp[sz-1] > 0


    def stoneGame_bottomup_2d(self, piles: List[int]) -> bool:
        ## with dp, time n^2
        
        sz = len(piles)
        dp = [ [0]*sz for _ in range(sz)]
        visited = [ [0]*sz for _ in range(sz)]
        for i in range(sz):
            dp[i][i] = piles[i]
        
        for L in range(1,sz):
            for i in range(sz-L):
                j = i+L
                dp[i][j] = max(piles[i] - dp[i+1][j], 
                              piles[j] - dp[i][j-1])
        return dp[0][sz-1]>0
        
    def stoneGame_topdown(self, piles: List[int]) -> bool:
        ## use relative score
        ## basically, the person who is moving now, is trying to get more than next person
        ##
        
        ## without dp, time = 2^n, with dp, time = n^2
        def searching(piles,dp,i,j):
            if i>j or j>= len(piles) or i<0:
                return 0
            if visited[i][j] >0:
                return dp[i][j]
            visited[i][j] = 1

            ## without dp, we can think of the speed as:
            ##  S(i,j) = S(i-1,j)  + S(i,j-1) = 2S(i,j-1)
            ## S(0,sz) = 2S(0,sz-1) =...= 2^sz
            ## Thus, speed without dp = 2^sz
            dp[i][j] = max(
                piles[i]-searching(piles,dp,i+1,j) ,
                piles[j]-searching(piles,dp,i,j-1))
            return dp[i][j]
        
        sz = len(piles)
        dp = [ [0]*sz for _ in range(sz)]
        visited = [ [0]*sz for _ in range(sz)]
        for i in range(sz):
            dp[i][i] = piles[i]
            
        res = searching(piles,dp,0,sz-1)
            
        return res>0