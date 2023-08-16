class Solution {
public:
    vector<vector<int>> res;
    vector<int> list;
    int sum = 0;
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        backtracking(candidates, target, 0);
        
        return res;
    }

    void backtracking(vector<int>& candidates, int target, int start) {
        if (sum == target) {
            vector<int> copy = list;
            res.push_back(list);
            return;
        }


        for (int i = start; i < candidates.size(); i++) {
            if (sum + candidates[i] > target) {
                break;
            }
            list.push_back(candidates[i]);
            sum += candidates[i];
            backtracking(candidates, target, i);
            sum -= candidates[i];
            list.pop_back();
        }
    }
};