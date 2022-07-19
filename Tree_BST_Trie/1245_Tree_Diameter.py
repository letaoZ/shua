
'''
1245. Tree Diameter
Medium

582

13

Add to List

Share
The diameter of a tree is the number of edges in the longest path in that tree.

There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the tree.

Return the diameter of the tree.

 

Example 1:


Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: The longest path of the tree is the path 1 - 0 - 2.
Example 2:


Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 

Constraints:

n == edges.length + 1
1 <= n <= 104
0 <= ai, bi < n
ai != bi
'''

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        for a,b in edges:
            g[a].add(b)
            g[b].add(a)
        
        ## NOTE: any node can be treated as root
        n = len(edges) + 1
        height = [0]*(n)
        res = [0]
        def geth(parnode,node, res):
            
            
            if not g[node]:
                height[node] = 1
                return 1
            
            if height[node]>0:
                return g[node]
        
            hts = []
            for child in g[node]:
                if child == parnode:
                    continue
                if height[child]>0:
                    continue
                hc = geth(node,child,res)
                heapq.heappush(hts, -hc)
            # print(height)
            height[node] = -heapq.heappop(hts) + 1 if hts else 1
            
            if len(hts) == 0:
                res[0] = max(height[node]-1,res[0])
            else:
                res[0] = max(res[0], height[node] -1 - heapq.heappop(hts) )
                
            return height[node]
        # print(height)
        
        geth(-1, 0, res)
        return res[0]