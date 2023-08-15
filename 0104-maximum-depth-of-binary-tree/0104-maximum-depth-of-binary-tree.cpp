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
    int maxDepth(TreeNode* root) {
        traverse(root, 0);
        return max;
    }

    void traverse(TreeNode* curr, int depth) {
        if (curr != NULL) {
            if (depth + 1 > max) {
                max = depth + 1;
            }

            traverse(curr->left, depth + 1);
            traverse(curr->right, depth + 1);
        }
    }
};