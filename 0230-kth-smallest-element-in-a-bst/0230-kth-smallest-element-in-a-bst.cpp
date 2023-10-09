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
    int res = 0;
    int kthSmallest(TreeNode* root, int k) {
        if (!root) {
            return 0;
        }
        
        kthSmallest(root->left, k);
        
        count++;
        if (count == k) {
            res = root->val;
            return res;
        }

        kthSmallest(root->right, k);

        return res;
    }
};