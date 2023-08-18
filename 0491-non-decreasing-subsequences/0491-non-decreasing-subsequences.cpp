class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        backtracking(nums, 0);
        return res;
    }

    void backtracking(vector<int>& nums, int start) {
        if (path.size() > 1) {
            vector<int> copy = path;
            res.push_back(copy);
        }
        
        unordered_set<int> set;
        for (int i = start; i < nums.size(); i++) {
            if (set.find(nums[i]) != set.end()) {
                continue;
            }
            set.insert(nums[i]);
            if (path.empty() || nums[i] >= path[path.size() - 1]) {
                path.push_back(nums[i]);
                backtracking(nums, i + 1);
                path.pop_back();
            }
        }
    }
};