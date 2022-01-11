'''
1319. Number of Operations to Make Network Connected
Medium

1665

26

Add to List

Share
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
 

Constraints:

1 <= n <= 105
1 <= connections.length <= min(n * (n - 1) / 2, 105)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.
'''
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ## n nodes need at least n-1 edges
        if len(connections) < n - 1:
            return -1
        
        ## build a connections graph (undirected); no repeated connections.
        graph = collections.defaultdict(set)
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)
        ## number of connected components gives extra_wire
        components = 0
        visited = [0]*n
        ## shortest path
        
        
        for i in range(n):
            if visited[i]:
                continue
                
            visited[i] = 1
            if i not in graph:
                components += 1
                continue
            
            queue = collections.deque()
            queue.append(i)
            
            while queue:
                cur = queue.popleft()
                for node in graph[cur]:
                    if visited[node]:
                        continue
                    visited[node] = 1
                    queue.append(node)
            components += 1
            
        return components-1
                            