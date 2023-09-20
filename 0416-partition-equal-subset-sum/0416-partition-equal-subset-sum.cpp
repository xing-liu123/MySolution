class Solution {
public:
    bool canPartition(vector<int>& nums) {
        if (nums.size() == 1) {
            return false;
        }

        if (nums.size() == 2) {
            return nums[1] == nums[0];
        }

        int sum = 0;

        for (int num : nums) {
            sum += num;
        }

        if (sum % 2 != 0) {
            return false;
        }

        int target = sum / 2;

        vector<int> dp(target + 1, 0);

        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                dp[i] = max(dp[i], dp[i - num] + num);
                if (dp[i] == target) {
                return true;
                }
            }

            
        }

        return dp[target] == target;

        return dp[target];
    }
};