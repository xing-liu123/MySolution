/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    let dp = Array(n + 1).fill(Number.MAX_SAFE_INTEGER);
    dp[0] = 0;
    
    for (let i = 1; i * i <= n; i++) {
        for (let j = 1; j <= n; j++) {
            if (i * i <= j) {
                dp[j] = Math.min(dp[j], dp[j - i * i] + 1);
            }
        }
    }
    
    return dp[n];
};