

## topological sort
#%%

import collections
List = list
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        ## define a Directed graph
        ## for each color c
        ##      find c's upper left and lower right corner
        ##      in c's rectangle, if there is any other color, we can paint them "later" than c
        ##      so there is an edge between c and all colors in its rectangle
        
        visited = {}
        graph = collections.defaultdict(set)
        M, N = len(targetGrid), len(targetGrid[0])
        for i in range(M):
            for j in range(N):
                c = targetGrid[i][j]
                if c in visited: continue
                ## Note: i,j here is upper left!
                visited[c] = 0
                ## upper left corner vs lower right corner
                upper, left, lower, right = float('inf'), float('inf'), -1, -1
                for x in range(M):
                    for y in range(N):
                        if targetGrid[x][y] == c:
                            upper = min(y, upper)
                            left =  min(x, left)
                            lower = max(lower, y)
                            right = max(right,x)

                for y in range(upper, lower+1):
                    for x in range(left, right + 1):
                        if targetGrid[x][y] != c:
                            graph[c].add(targetGrid[x][y])

        def dfs(graph, v):
            ## cycle
            if visited[v] == -1:
                return False
            if visited[v] == 1:
                return True 
            visited[v] = -1## if in dfs visit v again, means cycle
            for w in graph[v]:
                if not dfs(graph, w):
                    return False
            visited[v] = 1
            return True

        # print(graph)
        # print(visited)
        colors = list(visited.keys())
        for c in colors:
            if visited[c] == 1:
                continue
            if not dfs(graph,c):
                # print(c)
                # print(visited)
                return False
        return True
                        


    def isPrintable1(self, targetGrid: List[List[int]]) -> bool:
        visited = [0] * 61
        graph = collections.defaultdict(set)
        m, n = len(targetGrid), len(targetGrid[0])
        for c in range(1, 61):
            l,r,t,b = n,-1,m,-1
			#to specify the covered range of color c
            for i in range(m):
                for j in range(n):
                    if targetGrid[i][j] == c:
                        l = min(l, j)
                        r = max(r, j)
                        t = min(t, i)
                        b = max(b, i)
			#to find the contained colors
            for i in range(t, b + 1):
                for j in range(l, r + 1):
                    if targetGrid[i][j] != c:
                        graph[targetGrid[i][j]].add(c)
        
		# to find if there is a cycle 
        def dfs(graph,i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True 
            visited[i] = -1
            for j in graph[i]:
                if not dfs(graph,j):
                    return False
            visited[i] = 1
            return True
        
        for c in range(61):
            if not dfs(graph,c):
                return False
        return True



solu = Solution()
targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
solu.isPrintable(targetGrid)
# %%
