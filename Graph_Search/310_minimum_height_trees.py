'''
310. Minimum Height Trees
Medium

4789

195

Add to List

Share
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.

'''


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ## compute height for each node..
        ## very brutal.... time = n* (n**2)
        if n==1:
            return [0]
        g = collections.defaultdict(set)
        degree = [0]*n
        for a,b in edges:
            g[a].add(b)
            g[b].add(a)
            
            degree[a] += 1
            degree[b] += 1
            
        ## NOTE: if we only have a leaf node, that node is the min height tree
        ## and the height of a tree is the longest path from its root to leaf
        ## we need to find the "middle node(s)" in the longest path between two leaf node
        
        
        ## all leaf nodes
        queue = collections.deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
                degree[i] = 0
        res = []
        while queue:
            L = len(queue)
            res = []
            for _ in range(L):
                node = queue.popleft()
                res.append(node)
                for v in g[node]:
                    degree[v] -= 1
                    if degree[v] == 1:
                        queue.append(v)
                        
        return res
        

    def findMinHeightTrees_bfs_everytime(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        ## compute height for each node..
        ## very brutal.... time = n* (n**2)
        
        g = collections.defaultdict(set)
        for a,b in edges:
            g[a].add(b)
            g[b].add(a)
            
            
        def bfs(head, n, g):
            
            queue = collections.deque()
            queue.append(head)
            height = 0
            visited = [0]*n
            visited[head] = 1
            while queue:
                height += 1
                L = len(queue)
                for _ in range(L):
                    node = queue.popleft()
                    for k in g[node]:
                        if visited[k]:
                            continue
                        visited[k] = 1
                        queue.append(k)
                
            return height
        
        min_height = n
        roots = []
        for head in range(n):
            height = bfs(head, n, g)
            if height < min_height:
                min_height = height
                roots = [head]
            elif height == min_height:
                roots.append(head)
            else:
                pass
            
        return roots