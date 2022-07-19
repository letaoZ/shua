'''
1522. Diameter of N-Ary Tree
Medium

388

6

Add to List

Share
Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

(Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Explanation: Diameter is shown in red color.
Example 2:



Input: root = [1,null,2,null,3,4,null,5,null,6]
Output: 4
Example 3:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 7


'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        heights = collections.defaultdict(int) ## each node will have a list of children height
        res = [0]
        def get_height(node,res):
            if not node.children:
                heights[node] = 1
                return 1
            if heights[node]>0:
                return heights[node]
            hcs =  []
            
            for chld in node.children:
                hc = get_height(chld,res)
                heapq.heappush(hcs, -hc)
                # hcs.append(hc)
            # print(f"hcs {hcs}")
            M = -heapq.heappop(hcs)
            heights[node] = M+1
            if len(hcs) == 0:
                res[0] = max(heights[node]-1, res[0])## distance is number of edges between nodes... 
            else:
                max_path = M - heapq.heappop(hcs) + 1 - 1## distance is number of edges between nodes... 
                res[0] = max(max_path, res[0])
            return heights[node]
        
        get_height(root, res)
        # print(heights)
        return res[0]
        
        ## then we can take sum of left