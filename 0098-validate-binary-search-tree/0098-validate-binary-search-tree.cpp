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
    TreeNode* max;
    bool isValidBST(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }

        bool left = isValidBST(root->left);

        if (!left) {
            return false;
        }

        if (max != nullptr && root->val <= max->val) {
            return false;
        }

        max = root;

        return isValidBST(root->right);
        

    }

};