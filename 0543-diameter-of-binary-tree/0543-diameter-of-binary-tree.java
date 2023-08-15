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
    int max = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        traverse(root);
        return max;
    }

    private int traverse(TreeNode curr) {
        if (curr == null) {
            return 0;
        } else {
            int leftDepth = traverse(curr.left);
            int rightDepth = traverse(curr.right);

            if (leftDepth + rightDepth> max) {
                max = leftDepth + rightDepth;
            }

            return 1 + Math.max(leftDepth, rightDepth);
        }
    }
}