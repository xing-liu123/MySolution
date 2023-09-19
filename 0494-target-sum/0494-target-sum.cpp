class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum = 0;
        
        for (int num : nums) {
            sum += num;
        }

        // x - (sum - x) = target -> x = (sum + target) / 2;
        if (target < 0 && sum < -target) {
            return 0;
        }

        if ((sum + target) % 2 != 0) {
            return 0;
        }

        int myTarget = abs((sum + target) / 2);

        vector<int> dp(myTarget + 1, 0);
        dp[0] = 1;

        for (int num : nums) {
            for (int i = myTarget; i >= num; i--) {
                dp[i] += dp[i - num];
            }
        }

        return dp[myTarget];
    }
};