
'''
174. Dungeon Game
Hard


The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

 

Example 1:


Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
Example 2:

Input: dungeon = [[0]]
Output: 1
 

Constraints:

m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000


'''



## important: blood later cannot help blood now!!!
List = list()
class Solution:

    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        ## most recent submission 2022-01-31
        ## Time = O(MN), 
        m, n = len(grid), len(grid[0])
        
        ## dp[i][j] := blood needed if starting at cell [i][j]
        dp = [ [float('inf')] * (n+1) for _ in range(m+1)]
        
        ## just to be used as initial case
        dp[m][n-1] = dp[m-1][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(1, -grid[i][j] + min(dp[i+1][j], dp[i][j+1]))
        return dp[0][0]
    
    
    def calculateMinimumHP_formal_DP_bottomup(self, g: List[List[int]]) -> int:
        
        
        M,N = len(g), len(g[0])
        
        def searching(g,i,j,dp):
            
            if i==M-1 and j==N-1:
                dp[i][j] = max(-g[i][j]+1, 1)
                return dp[i][j]
            
            if i<0 or j<0 or i>=M or j >= N:
                return float('inf')
            
            if dp[i][j] < float('inf'):
                return dp[i][j]
            
            ## Note:
            cur_need = -g[i][j]
            addition = min(searching(g,i,j+1,dp), searching(g,i+1,j,dp))
            if addition == float('inf'):
                return addition
            
            
            dp[i][j] = max(cur_need + addition,1)
            return dp[i][j]

        ## if starting from i,j, 
        ## min health NEEDED as dp[i][j]    
        ## if NEEDED is negative, then "extra we have"
        dp = [ [float('inf')]*(N) for _ in range(M) ]
        res = searching(g,0, 0,dp)


        return dp[0][0]


        
    def calculateMinimumHP_memoization_topdown(self, g: List[List[int]]) -> int:
        ## memoization top down
        M,N = len(g), len(g[0])
        ## dp cushion
        ## dp[i][j] min blood need starting from i,j till the prince
        dp = [ [float('inf')]*(N+1) for _ in range(M+1) ]
        dp[-1][N-1] = dp[M-1][-1] = 1
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                dp[i][j] = max(min( dp[i+1][j], dp[i][j+1] ) - g[i][j], 1)
                
        return dp[0][0]    
    
    
    def calculateMinimumHP_memoization_topdown_memReduction(self, g: List[List[int]]) -> int:
        ## memoization top down dimension reduction

        M,N = len(g), len(g[0])
        ## dp cushion
        ## dp[i][j] min blood need starting from i,j till the prince
        dp = [float('inf')]*(N+1)
        dp[N-1] = 1
        for i in range(M-1,-1,-1):
            dp_tmp = [kk for kk in dp]
            for j in range(N-1,-1,-1):
                ## important step
                dp[j] = max(min( dp_tmp[j], dp[j+1] ) - g[i][j], 1)
        
        return dp[0]        

        

g = [[-1]]
g = [[0]]
g = [[-1,1,-1]]
g = [[-2,-3],[2,2]]
g = [[-2,-3],[2,-2]]

solu = Solution()
solu.calculateMinimumHP_formal_DP_bottomup(g)

