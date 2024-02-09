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
    public List<Integer> path;
    public List<List<Integer>> res;
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        path = new ArrayList<>();
        res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        path.add(root.val);
        backtrack(root, targetSum - root.val);
        return res;
    }
    
    private void backtrack(TreeNode node, int targetSum) {
        if (node.left == null && node.right == null && targetSum == 0) {
            res.add(new ArrayList<>(path));
            return;
        }
        
        if (node.left != null) {
            path.add(node.left.val);
            backtrack(node.left, targetSum - node.left.val);
            path.remove(path.size() - 1);
        }
        
        if (node.right != null) {
            path.add(node.right.val);
            backtrack(node.right, targetSum - node.right.val);
            path.remove(path.size() - 1);
        }
    }
}