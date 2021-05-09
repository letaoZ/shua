



## max cherries
## dp[x][y][x1] 
### -- robot left starting at x,y, and robot right starting at (x+y)-x1
### max total they get
#%%
List = list

class Solution:
    def cherryPickup_topdown_dimRuduction_more(self, g: List[List[int]]) -> int:
        M, N = len(g), len(g[0])

        ## adding cushion
        dp = [[-1]*(N+1) for _ in range(N+1)]
        
        ## the extra row: dp[M][:N][:N] will have zero  values
        for i in range(N):
            for j in range(N):
                dp[i][j] = 0
        
        
        ## dp[x][y][y1] -- > total is M-1 steps, x always increase by 1
        ## reduce x
        
        for x in range(M-1,-1,-1):
            dp_tmp = [[dp[i][j] for i in range(N+1)] for j in range(N+1) ]
            for y in range(N-1,-1,-1):
                for y1 in range(N-1,-1,-1):
        
        
                    tmp = max(dp_tmp[y-1][y1], dp_tmp[y-1][y1-1],dp_tmp[y-1][y1+1], 
                              dp_tmp[y][y1], dp_tmp[y][y1-1],dp_tmp[y][y1+1],
                              dp_tmp[y+1][y1], dp_tmp[y+1][y1-1],dp_tmp[y+1][y1+1], 
                             )
                    if tmp == -1: 
                        continue
            
                    dp[y][y1] = tmp + g[x][y]
                    if y!=y1:
                        dp[y][y1] += g[x][y1]
        
        
        return dp[0][N-1]

    
    def cherryPickup_topdown_dimRuduction(self, g: List[List[int]]) -> int:
        M, N = len(g), len(g[0])

        ## adding cushion
        dp = [[[-1]*(N+1) for _ in range(N+1)] for _ in range(M+1)]
        
        ## the extra row: dp[M][:N][:N] will have zero  values
        for i in range(N):
            for j in range(N):
                dp[M][i][j] = 0
        
        ## eg: 
        ## g =[[1,2], 
        #     [3,4]]
        ## g'=[[1,2,-1],   (with cusion) 
        #      [3,4,-1],
        #      [0,0,-1]]
        
        ## dp[x][y][y1] -- > total is M-1 steps, x always increase by 1
        
        for x in range(M-1,-1,-1):
            for y in range(N-1,-1,-1):
                for y1 in range(N-1,-1,-1):
        
        
                    tmp = max(dp[x+1][y-1][y1], dp[x+1][y-1][y1-1],dp[x+1][y-1][y1+1], 
                              dp[x+1][y][y1], dp[x+1][y][y1-1],dp[x+1][y][y1+1],
                              dp[x+1][y+1][y1], dp[x+1][y+1][y1-1],dp[x+1][y+1][y1+1], 
                             )
                    if tmp == -1: 
                        continue
            
                    dp[x][y][y1] = tmp + g[x][y]
                    if y!=y1:
                        dp[x][y][y1] += g[x][y1]
        
        
        return dp[0][0][N-1]
        
    def cherryPickup_4dim_bottomUp(self, g: List[List[int]]) -> int:
        M, N = len(g), len(g[0])

        def out_of_bound(x, high_bound):
            if x<0 or x>= high_bound:
                return True
            else:
                return False
        def searching(g, x, y, x1,y1, dp):

            if (
                out_of_bound(x,M) or 
                out_of_bound(y,N) or 
                out_of_bound(x1,M) or
                out_of_bound(y1,N) 
            ):
                return -1

            if x == M-1 and x1 == M-1:
                dp[x][y][x1][y1] = g[x][y]
                if y!=y1:
                    dp[x][y][x1][y1] += g[x1][y1]

            if dp[x][y][x1][y1] >=0 :
                return dp[x][y][x1][y1]

            tmp = max(
                searching(g, x+1,y-1, x1+1,y1,dp), 
                searching(g, x+1,y, x1+1,y1,dp), 
                searching(g, x+1,y+1, x1+1,y1,dp), 

                searching(g, x+1,y-1, x1+1,y1-1,dp), 
                searching(g, x+1,y, x1+1,y1-1,dp), 
                searching(g, x+1,y+1, x1+1,y1-1,dp), 

                searching(g, x+1,y-1, x1+1,y1+1,dp), 
                searching(g, x+1,y, x1+1,y1+1,dp), 
                searching(g, x+1,y+1, x1+1,y1+1,dp), 
            )

            if tmp == -1:
                return -1

            dp[x][y][x1][y1] = tmp
            dp[x][y][x1][y1] += g[x][y]
            if (x,y)  != (x1, y1):
                dp[x][y][x1][y1] += g[x1][y1]

            return dp[x][y][x1][y1]

        res = 0

        dp = [[[[-1]*(N) for _ in range(M)] for _ in range(N)] for _ in range(M)]
        res = max(res, searching(g, 0, 0, 0,N-1, dp))
        return (res)

g = [
    [3,1],
    [3,1],]
# g= [[0]]
# g = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
M, N = len(g), len(g[0])

solu = Solution()
solu.cherryPickup_topdown_dimRuduction_more(g)
# %%
