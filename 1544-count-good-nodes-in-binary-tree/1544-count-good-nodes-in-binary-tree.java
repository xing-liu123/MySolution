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
    int count = 0;
    public int goodNodes(TreeNode root) {
        traverse(root, Integer.MIN_VALUE);
        return count;
    }

    private void traverse(TreeNode curr, int max) {
        if (curr == null) {
            return;
        }

        if (curr.val >= max) {
            count++;
            max = curr.val;
        }

        traverse(curr.left, max);
        traverse(curr.right, max);
    }
}