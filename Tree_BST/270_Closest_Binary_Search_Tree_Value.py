'''
270. Closest Binary Search Tree Value
Easy

1392

86

Add to List

Share
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

 

Example 1:


Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
Example 2:

Input: root = [1], target = 4.428571
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 109
-109 <= target <= 109

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue_recur(self, root: Optional[TreeNode], target: float) -> int:
        
        delta = [float("inf")]
        res = [-1]
        def searching(node, target, delta, res):
            if node is None: return
            
            dff = target - node.val
            if abs(dff) < delta[0]:
                delta[0] = abs(dff)
                res[0] = node.val
                
            if delta[0] == 0: return
                      
            if dff < 0:
                searching(node.left, target, delta, res)
            else:
                searching(node.right, target, delta, res)
                      
                    
        
        searching(root, target, delta, res)
        return res[0]
    # def closestValue_iter(self, root: Optional[TreeNode], target: float) -> int:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        delta =float("inf")
        res = -1
        while root:
            dff = root.val - target
            if abs(dff) < delta:
                res = root.val
                delta = abs(dff)
            if delta == 0: return res
            if dff > 0: root = root.left
            else: root = root.right        
        return res