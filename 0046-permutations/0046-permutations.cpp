class Solution {
public:
    vector<vector<int>> res;
    vector<int> list;
    vector<int> used;
    vector<vector<int>> permute(vector<int>& nums) {
       used = vector<int>(nums.size(), 0);
        backtracking(nums);
        return res;
    }

    void backtracking(vector<int>& nums) {
        if (list.size() == nums.size()) {
            vector<int> copy = list;
            res.push_back(copy);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (used[i] == 1) {
                continue;
            }
            used[i] = 1;
            list.push_back(nums[i]);
            backtracking(nums);
            used[i] = 0;
            list.pop_back();
        }
    }
};