class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;
    int sum = 0;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        backtracking(candidates, target, 0);
        return res;
    }

    void backtracking(vector<int>& candidates, int target, int start) {
        if (sum == target) {
            vector<int> copy = path;
            res.push_back(copy);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            int val = candidates[i];
            if (sum + val > target) {
                break;
            }

            if (i != start && val == candidates[i - 1]) {
                continue;
            }

            path.push_back(val);
            sum += val;
            backtracking(candidates, target, i + 1);
            sum -= val;
            path.pop_back();

        }
    }
};