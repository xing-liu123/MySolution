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
    bool res = true;
    bool isBalanced(TreeNode* root) {
        traverse(root);
        return res;
    }

    int traverse(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }

        int left = traverse(root->left);

        int right = traverse(root->right);

        if (abs(left - right) > 1) {
            res = false;
        }

        return max(left, right) + 1;
    }
};