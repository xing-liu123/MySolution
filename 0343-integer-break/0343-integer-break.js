/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {
    const dp = new Array(n + 1).fill(0);
    
    dp[2] = 1;
    
    for (let i = 3; i <= n; i++) {
        for (let j = 1; j <= i - j; j++) {
            dp[i] = Math.max(Math.max(j * (i - j), dp[i - j] * j), dp[i]);
        }
    }
    
    return dp[n];
};