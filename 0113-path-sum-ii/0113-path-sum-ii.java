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

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        
        if (root != null) {
            backtrack(root, targetSum, path, res);
        }
        
        return res;
    }
    
    private void backtrack(TreeNode node, int targetSum, List<Integer> path, List<List<Integer>> res) {
        path.add(node.val);
        
        if (node.left == null && node.right == null && node.val == targetSum) {
            res.add(new ArrayList<>(path));
        } else {
            if (node.left != null) {
                backtrack(node.left, targetSum - node.val, path, res);
            }
            
            if (node.right != null) {
                backtrack(node.right, targetSum - node.val, path, res);
            }
        }
        
        path.remove(path.size() - 1);
    }
}