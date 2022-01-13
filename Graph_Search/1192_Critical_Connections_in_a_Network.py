## cycle detection in a undirected graph
## DFS

'''
1192. Critical Connections in a Network
Hard

3223

135

Add to List

Share
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
'''

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ## if an edge is on a cycle,it is safe
        
        G = collections.defaultdict(set)
        noncritical_edges = collections.defaultdict(int)
        for i,(a, b) in enumerate(connections):
            G[a].add(b)
            G[b].add(a)
            if a<b:
                noncritical_edges[(a,b)] = 0
            else:
                noncritical_edges[(b,a)] = 0
        rk = [-2]*n ## -2 means never been visited. we use this number to distinguish depth values 
        def dfs(v_from, v,rk_v, rk):
            # print(f"dfs from {v_from},to {v}")
            if rk[v]>=0:
                return rk[v]
            rk[v] = rk_v
            for w in G[v]:
                if w==v_from:
                    continue
                rk_w = dfs(v,w,rk_v+1,rk)
                if rk_w <= rk_v:
                    # print(f"rk_w <= rk_v: v={v} rk {rk_v}, w={w} rk {rk_w}, ")
                    # print()
                    if w<v:
                        noncritical_edges[(w,v)] = 1
                    else:
                        noncritical_edges[(v,w)] = 1
                    rk[v]  = min(rk[v] ,rk_w)
            return rk[v] 
        dfs(0,0,0,rk)
        # print(rk)
        return [[a,b] for (a,b),v in noncritical_edges.items() if v==0]