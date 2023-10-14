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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }

        if (root.val > val) {
            root.left =  insertIntoBST(root.left, val);
        } else {
            root.right =  insertIntoBST(root.right, val);
        }

        return root;
    }

    // private TreeNode insert(TreeNode curr, int val) {
    //     if (curr == null) {
    //         return new TreeNode(val);
    //     } else if (curr.val < val) {
    //         curr.right = insert(curr.right, val);
    //     } else if (curr.val > val) {
    //         curr.left = insert(curr.left, val);
    //     }

    //     return curr;
    // }
}