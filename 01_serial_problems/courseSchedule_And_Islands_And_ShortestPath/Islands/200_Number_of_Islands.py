
import collections


class Solution:

    def numIslands_unionFind(self, grid):
        ## tbd
        return

    def numIslands_bfs(self, grid):
        ## bfs: log(V+E): V=m*n, E ~~ 4*V --> time = O(MN)
        M, N = len(grid), len(grid[0])

        cnt = 0
        
        for i in range(M):
            for j in range(N):
                
                if grid[i][j] == "0":
                    continue
                
                q = collections.deque()        
                q.append( (i,j) )
                print(i,j)
                while(q):
                    x, y = q.popleft()
                    grid[x][y] = "0"
                    for (dx,dy) in [(0,1),(0,-1),(1,0),(-1,0)]:
                        x1, y1 = x+dx, y+dy
                        if x1<0 or y1<0 or x1>= M or y1 >= N:
                            continue
                        if grid[x1][y1] == "1":
                            q.append( (x1,y1))
                cnt += 1
        return cnt


    def numIslands_dfs_noExtraSpace(self, grid):
        ## number of connected components
        ## dfs: log(V+E): V=m*n, E ~~ 4*V --> time = O(MN)
        M, N = len(grid), len(grid[0])

        def dfs(grid, i, j):
            if grid[i][j] == "v": ## "v" stands for visited
                return

            if grid[i][j] == "0":
                grid[i][j] = "v"
                return

            grid[i][j] = "v"
            for (dx,dy) in [(0,1),(0,-1),(1,0),(-1,0)]:
                x,y = i+dx, j+dy
                if x<0 or y<0 or x>= M or y>= N:
                    continue
                dfs(grid,x,y)

            return 

        cnt = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]=="1":
                    dfs(grid, i,j)
                    cnt += 1
        return cnt

    def numIslands_dfs(self, grid):
        ## number of connected components
        ## dfs: log(V+E): V=m*n, E ~~ 4*V --> time = O(MN)
        M, N = len(grid), len(grid[0])
        visited = [[0]*N for _ in range(M)]

        def dfs(grid, visited, i, j):
            if visited[i][j] == 1:
                return
            visited[i][j] = 1

            if grid[i][j] == "0":
                return

            for (dx,dy) in [(0,1),(0,-1),(1,0),(-1,0)]:
                x,y = i+dx, j+dy
                if x<0 or y<0 or x>= M or y>= N:
                    continue
                dfs(grid,visited,x,y)

            return 

        cnt = 0
        for i in range(M):
            for j in range(N):
                if visited[i][j] == 0 and grid[i][j]=="1":
                    dfs(grid, visited, i,j)
                    cnt += 1
        return cnt



grid = [
  ["1","1","0","1","0"],
  ["1","0","1","1","0"],
  ["1","1","1","0","1"],
  ["0","0","0","0","1"]
]

solu = Solution()
solu.numIslands_unionFind(grid)