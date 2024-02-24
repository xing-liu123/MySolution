/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    if (amount === 0) {
        return 0;
    }
    
    let dp = Array(amount + 1).fill(Number.MAX_SAFE_INTEGER);
    dp[0] = 0;
    
    for (let i = 0; i < coins.length; i++) {
        for (let j = 1; j <= amount; j++) {
            if (j >= coins[i]) {
                dp[j] = Math.min(dp[j], dp[j - coins[i]] + 1);
            }
        }
    }
    
    return dp[amount] === Number.MAX_SAFE_INTEGER ? -1 : dp[amount];
};