class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();

        if (n == 1) {
            return nums[0];
        }
        vector<int> earns(n, 0);

        earns[0] = nums[0];
        earns[1] = max(nums[0], nums[1]);

        for (int i = 2; i < n; i++) {
            earns[i] = max(earns[i - 1], earns[i - 2] + nums[i]);
        }

        return earns[n - 1];
    }
};