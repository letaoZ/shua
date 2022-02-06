'''
863. All Nodes Distance K in Binary Tree
Medium

5316

111

Add to List

Share
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ## for each node find its parent node and build a graph
        ## we assume nodes values are unique; the graph can be built using values
        graph = collections.defaultdict(list)
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node.left.val].append(node.val)
                graph[node.val].append(node.left.val)
                queue.append(node.left)
            if node.right:
                graph[node.right.val].append(node.val)
                graph[node.val].append(node.right.val)
                queue.append(node.right)
                
                
                
        ## so we can search beginning from target till we reach level k
        queue = collections.deque()
        queue.append(target.val)
        visited = [target.val]
        for _ in range(k):
            L = len(queue)
            for _ in range(L):
                v = queue.popleft()
                for nv in graph[v]:
                    if nv in visited: continue
                    queue.append(nv)
                    visited.append(nv)
        
        return list(queue)

    def distanceK_dfs(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ## build a graph using the tree
        
        g = collections.defaultdict(set)
        queue = collections.deque()
        queue.append(root)
        while queue:
            L = len(queue)
            for _ in range(L):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                    g[node.val].add(node.left.val)
                    g[node.left.val].add(node.val)
                if node.right:
                    queue.append(node.right)
                    g[node.val].add(node.right.val)
                    g[node.right.val].add(node.val)
        
        res = []
        visited = []
        def dfs(val,k_remain):
            if val in visited:
                return
            if k_remain == 0:
                res.append(val)
            
            for w in g[val]:
                dfs(w,k_remain - 1)
        
        
        dfs(target,k)
        return res
                
