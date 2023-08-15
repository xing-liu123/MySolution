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
        traverse(root, 0);
        return max;
    }

    private int traverse(TreeNode curr, int depth) {
        if (curr == null) {
            return depth;
        } else {
            int leftDepth = traverse(curr.left, depth + 1);
            int rightDepth = traverse(curr.right, depth + 1);

            if (leftDepth + rightDepth - 2*(depth + 1) > max) {
                max = leftDepth + rightDepth - 2*(depth + 1);
            }

            return Math.max(leftDepth, rightDepth);
        }
    }
}