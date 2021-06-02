

List = list
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        def searching(grid,i,j,cnt):
            if i>=M or j>= N or i<0 or j<0:
                return 

            if grid[i][j] == 0:
                return 

            grid[i][j] = 0
            cnt[0] += 1

            for dx, dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                x,y = i + dx, j + dy

                searching(grid,x,y,cnt)

        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]==1:
                    cnt = [0]
                    searching(grid,i,j,cnt)
                    res = max(res, cnt[0])
        return res

grid = [[0,1], 
        [1,1],
        [0,0],
        [1,1]]