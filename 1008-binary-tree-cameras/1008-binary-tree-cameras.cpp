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
    int count = 0;
    int minCameraCover(TreeNode* root) {
        int res = min(root);
        if (res == 0) {
            return count + 1;
        } else {
            return count;
        }
    }

    int min(TreeNode* root) {
        if (root->left == NULL && root->right == NULL) {
            return 0;
        }

        int left = -1;
        int right = -1;

        if (root->left != NULL) {
            left = min(root->left);
        }
        
        if (root->right != NULL) {
            right = min(root->right);
        }

        if (left == 0 || right == 0) {
            count++;
            return 2;
        }

        if (left == 2 || right == 2) {
            return 1;
        }

        return 0;
 
    }
};