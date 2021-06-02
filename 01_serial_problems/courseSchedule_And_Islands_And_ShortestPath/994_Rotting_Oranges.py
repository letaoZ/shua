
import collections

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        freshn = 0
        q = collections.deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    freshn += 1
        if freshn == 0:
            return 0

        ## count the number of rottening fresh oranges
        cnt = 0

        ## count number of minutes
        minutes = -1    
        ## NOTE: freshn now is >0. If there isn't any rotten ones, then return -1, 
                
        dir = [(0,1),(0,-1), (1,0), (-1,0)]

        ## bft gives shortest path, so we needt o use it to find smallest minutes
        while q:
            L = len(q)
            for _ in range(L):
                x,y = q.popleft()
                for dx, dy in dir:
                    x1, y1 = x+dx, y+dy
                    if x1>=M or y1>=N or x1<0 or y1<0:
                        continue
                    if grid[x1][y1] != 1:
                        continue
                    grid[x1][y1] = 2 ## fresh --> not fresh
                    q.append((x1,y1))
                    cnt += 1
            minutes += 1


        print(cnt, freshn,minutes)
        if cnt<freshn:
            return -1

        return minutes

grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
    ]

grid = [
    [2,1,1],
    [1,1,0],
    [0,0,1]
    ]


solu = Solution()
solu.orangesRotting(grid)