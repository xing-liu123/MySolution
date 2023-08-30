class Solution {
public:
    int rob(vector<int>& nums) {
        int len = nums.size();
        if (len == 1) {
            return nums[0];
        } else if (len == 2) {
            return max(nums[0], nums[1]);
        }

        return max(rob(nums, 0, len - 2), rob(nums, 1, len - 1));
    }

    int rob(vector<int>& nums, int start, int end) {
        if (start == end) {
            return nums[start];
        }

        int x = nums[start];
        int y = max(x, nums[start + 1]);
        int z = 0;
        for (int i = start + 2; i <= end; i++) {
            z = max(y, x + nums[i]);
            x = y;
            y = z;

        }

        return y;
    }
};