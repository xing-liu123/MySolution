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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (root == NULL) {
            return false;
        }

        if (isEqual(root, subRoot)) {
            return true;
        }

        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }

    bool isEqual(TreeNode* root, TreeNode* subRoot) {
        if (root == NULL && subRoot == NULL) {
            return true;
        } else if (root == NULL || subRoot == NULL) {
            return false;
        }

        return root->val == subRoot->val && isEqual(root->left, subRoot->left) && isEqual(
            root->right, subRoot->right);
    }
};