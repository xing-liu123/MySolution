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
    void traverse(vector<vector<int>>& res, TreeNode* node, int depth){
        if (node == NULL) {
            return;
        }

        if (res.size() <= depth) {
            vector<int> list;
            res.push_back(list);
        } 

        res[depth].push_back(node->val);

        traverse(res, node->left, depth + 1);
        traverse(res, node->right, depth + 1);
    }
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        if (root == NULL) {
            return res;
        }

        traverse(res, root, 0);
        reverse(res.begin(), res.end());
        return res;
    }
};