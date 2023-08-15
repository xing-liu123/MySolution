/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int max = 0;
    int diameterOfBinaryTree(TreeNode* root) {
        traverse(root);
        return max;
    }

    int traverse(TreeNode* curr) {
        if (curr == NULL) {
            return 0;
        } else {
            int leftHeight = traverse(curr->left);
            int rightHeight = traverse(curr->right);

            max = std::max(max, leftHeight + rightHeight);

            return 1 + std::max(leftHeight, rightHeight);
        }
    }
};