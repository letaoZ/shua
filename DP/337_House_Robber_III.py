'''
337. House Robber III
Medium

5795

89

Add to List

Share
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:


Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:


Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 104
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob_mem_dp_dict(self, root: Optional[TreeNode]) -> int:
        
        
        dp = {} ## key = (if rob parent node, node)
        def searching(prev_robbed, node):
            
            cur_value = 0
            if node is None:
                return cur_value
            if (prev_robbed, node) in dp:
                return dp[(prev_robbed, node)]
            
            ## here we can always choose not to rob current node 
            ## this doesn't depend on whether the previous one is robbed or not
            

            cur_value_left = searching(False,node.left)
            cur_value_right = searching(False,node.right)
            cur_value = cur_value_left + cur_value_right
            
                
            if prev_robbed:
                pass ## you have no choice, but NOT to rob current node 
            else:        ## rob current node
                cur_value_left = searching(True,node.left)
                cur_value_right = searching(True,node.right)
                cur_value = max(cur_value, cur_value_left + cur_value_right + node.val)
            dp[(prev_robbed, node)] = cur_value
            return cur_value
        
        res1 = searching(False,root)
        res2 = searching(True, root)

        return max(res1, res2)
            
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {} ## key = node, value = pairs of (if_rob, if_not_rob)
        def searching(node):
            ## return [if rob current node max profit, if not rob current node max profit]
            if node in dp:
                return dp[node]
            if node is None:
                return 0, 0
            
            value_left = searching(node.left) ## [rob_left, not_rob_left]
            value_right = searching(node.right)## rob_right, not_rob_right
            
            ## if we rob current node, then we could only choose not_rob_left, not_rob_right
            rob_cur = node.val + value_left[1] + value_right[1]
            
            
            ## if we don't rob current node, then we are free to do whatever we need for left or right
            
            not_rob_cur = 0
            for i in range(2):
                for j in range(2):
                    not_rob_cur = max(not_rob_cur, value_left[i] + value_right[j])
            dp[node] = (rob_cur, not_rob_cur)
            return rob_cur, not_rob_cur
        
        res = searching(root)
        return max(res)