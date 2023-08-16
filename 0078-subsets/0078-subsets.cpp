class Solution {
public:
    vector<vector<int>> res;
    vector<int> list;
    vector<vector<int>> subsets(vector<int>& nums) {
        backtracking(nums, 0);
        return res;
    }

    void backtracking(vector<int>& nums, int start) {
        vector<int> copy = list;
        res.push_back(copy);

        if (start == nums.size()) {
            return;
        }

        for (int i = start; i < nums.size(); i++) {
            list.push_back(nums[i]);
            backtracking(nums, i + 1);
            list.pop_back();
        }
    }
};