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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (root == NULL) {
            return res;
        }

        deque<TreeNode*> queue;

        queue.push_back(root);

        while (!queue.empty()) {
            vector<int> list;
            int size = queue.size();

            while (size > 0) {
                TreeNode* node = queue.front();
                queue.pop_front();

                if (node->left != NULL) {
                    queue.push_back(node->left);
                }

                if (node->right != NULL) {
                    queue.push_back(node->right);
                }

                list.push_back(node->val);
                size--;
            }
            res.push_back(list);
        }

        return res;
    }
};