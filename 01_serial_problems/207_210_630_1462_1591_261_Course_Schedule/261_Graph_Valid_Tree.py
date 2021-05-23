
'''
261. Graph Valid Tree
Medium


You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
 

Constraints:

1 <= 2000 <= n
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.

A LOT of edge cases
'''



import collections

class Solution:

    def validTree(self, n:int, edges: list[list[int]]) -> bool:
        ## true means no cycle, valid tree
        ## false means cycle, 

        ## NOTE: a tree must be connected! must have n nodes...
        def searching(g,visited, prev, v):
            if visited[v] == 1:
                return True
            if visited[v] == -1:
                return False

            visited[v] = -1
            for w in g[v]:
                if w == prev: continue
                if not searching(g,visited,v,w):
                    return False

            visited[v] = 1
            return True
        
        if not edges:
            return n<=1

        g = collections.defaultdict(set)

        ## -1 means cycle
        ## 1 means visited
        ## 0 to be visited
        ## 10 no such node
        visited =[10]*n
        startNode = 0
        for a,b in edges:
            g[a].add(b)
            g[b].add(a)
            visited[a] = visited[b] = 0
            startNode = a

        for val in visited:
            if val == 10:
                return False


        res = True


        ## to be connected, need to make sure all nodes are visited after one pass
        res = searching(g,visited, -1, startNode)

        for val in visited:
            if val == 0:
                return False


        return res




n = 5
edges =[[0,1],[2,3]]
edges = []
solu = Solution()
solu.validTree(n, edges)