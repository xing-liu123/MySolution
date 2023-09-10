class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0) {
            return 0;
        }

        vector<int> dp(amount + 1, INT_MAX);

        for (int coin : coins) {
            if (coin <= amount) {
                 dp[coin] = 1;
            }
           
        } 

        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.size(); j++) {
                if (coins[j] <= amount && i - coins[j] >= 0 && dp[i - coins[j]] != INT_MAX) {
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1); 

                }
            }
        }

        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};