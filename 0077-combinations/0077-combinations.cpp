class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;
    vector<vector<int>> combine(int n, int k) {
        backtracking(1, n, k);
        return res;
    }

    void backtracking(int start, int n, int k) {
        if (path.size() == k) {
            vector<int> copy = path;
            res.push_back(copy);
            return;
        }

        for (int i = start; i <= n; i++) {
            path.push_back(i);
            backtracking(i + 1, n, k);
            path.pop_back();
        }
    }
};