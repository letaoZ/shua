
'''
323. Number of Connected Components in an Undirected Graph
Medium

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
'''

import collections

class Solution:
    def countComponents(self, n, edges):
        def searching(g,prev,v,visited):

            if visited[v] == 1:
                return 

            visited[v] = 1

            for w in g[v]:
                if w == prev: continue
                searching(g,v,w,visited)

        g = collections.defaultdict(set)
        visited = dict()
        for a,b in edges:
            g[a].add(b)
            g[b].add(a)
            visited[a] = visited[b] = 0

        print(g)
        cnt = 0
        ## note: if a node is not in an edge, assume it's one the graph
        ## n is given as number of nodes
        for v in range(n):
            if v not in visited:
                cnt += 1
                continue
            if visited[v] == 0:
                searching(g, -1, v, visited)
                cnt += 1

        return cnt


n = 10
edges = [[0,1],[1,2],[2,3],[3,4]]
edges = [[0,1], [1,2], [2,0], [2,3],[4,5] ]
solu  = Solution()
solu.countComponents(n, edges)
