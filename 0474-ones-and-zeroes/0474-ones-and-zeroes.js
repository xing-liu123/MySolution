/**
 * @param {string[]} strs
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var findMaxForm = function(strs, m, n) {
    let dp  = Array.from({length : m + 1}, () => Array(n + 1).fill(0));
    
    const countNumber = (str) => {
        const counts = {'0': 0, '1': 0};
        str.split('').forEach(char => {
            counts[char]++;
        })
        
        return counts;
    }
    
    for (let i = 0; i < strs.length; i++) {
        const counts = countNumber(strs[i]);
        let zeros = counts['0'];
        let ones = counts['1'];
        for (let j = m; j >= zeros; j--) {
            for (let k = n; k >= ones; k--) {
                dp[j][k] = Math.max(dp[j][k], dp[j - zeros][k - ones] + 1);
            }
        }
    }
    
    return dp[m][n];
};