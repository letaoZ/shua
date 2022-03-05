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
    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        List<Integer> ret = new ArrayList<>();
        if (root == null) return ret;
        
        ret.add(root.val);
        ArrayDeque<Integer> lbnodes = new ArrayDeque<>();
        ArrayDeque<Integer> rbnodes = new ArrayDeque<>();
        ArrayDeque<Integer> leafnodes = new ArrayDeque<>();
        
        if (root.left != null) lb(root.left, lbnodes);        
        if (root.right != null) rb(root.right, rbnodes);
        if (!isLeaf(root)) addLeaf(root, leafnodes);
        while (!lbnodes.isEmpty()) ret.add(lbnodes.pollFirst());
        while (!leafnodes.isEmpty()) ret.add(leafnodes.pollFirst());
        while (!rbnodes.isEmpty()) ret.add(rbnodes.pollLast());
        return ret;
    }
    
    public void lb(TreeNode lbNode, ArrayDeque<Integer> buf) {
        if (!isLeaf(lbNode)) buf.add(lbNode.val);
        else return;
        
        if (lbNode.left != null) lb(lbNode.left, buf);
        else lb(lbNode.right, buf);
    }
    
    public void rb(TreeNode rbNode, ArrayDeque<Integer> buf) {
        if (!isLeaf(rbNode)) buf.add(rbNode.val);
        else return;
        
        if (rbNode.right != null) rb(rbNode.right, buf);
        else rb(rbNode.left, buf);
    }
    
    public void addLeaf(TreeNode root, ArrayDeque<Integer> buf) {
        if (root == null) return;
        
        if (isLeaf(root)) buf.add(root.val);
        else {
            addLeaf(root.left, buf);
            addLeaf(root.right, buf);            
        }
    }  
    
    public boolean isLeaf(TreeNode node) {
        return (node.left == null && node.right == null);
    }
}