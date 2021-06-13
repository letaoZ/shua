/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int goodNodes(TreeNode root) {
        int[] counter = new int[1];        
        helper(root, Integer.MIN_VALUE, counter);        
        return counter[0];
    }
    
    
    private void helper(TreeNode root, int maxValue, int[] counter) {
        if (root == null) return;
        
        if (root.val >= maxValue) {
            counter[0]++;
            maxValue = root.val;
        }
        
        helper(root.left, maxValue, counter);
        helper(root.right, maxValue, counter);
    }
    
    
}