

## topological sort
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
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