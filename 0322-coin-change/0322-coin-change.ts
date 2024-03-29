function coinChange(coins: number[], amount: number): number {
    let dp : number[] = Array(amount + 1).fill(Number.MAX_SAFE_INTEGER);
    dp[0] = 0;
    
    for (let i = 1; i <= amount; i++) {
        for (let j = 0; j < coins.length; j++) {
            if (i >= coins[j]) {
                dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
            }
        }
    }
    
    return dp[amount] === Number.MAX_SAFE_INTEGER ? -1 : dp[amount];
};