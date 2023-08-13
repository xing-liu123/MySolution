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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        if (root == nullptr) {
            return res;
        }

        deque<TreeNode*> q;

        q.push_back(root);

        while(!q.empty()) {
            int size = q.size();
            vector<int> list;

            while(size > 0) {
                TreeNode* node = q.front();
                q.pop_front();
                
                list.push_back(node->val);

                if (node->left != nullptr) {
                    q.push_back(node->left);
                }

                if (node->right != nullptr) {
                    q.push_back(node->right);
                }

                size--;
            }
            res.insert(res.begin(), list);
            
        }

        return res;
    }
};