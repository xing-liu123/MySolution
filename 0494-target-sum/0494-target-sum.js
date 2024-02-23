/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var findTargetSumWays = function(nums, target) {
    let sum = 0;
    
    nums.forEach(num => sum += num);
    
    if (target < 0 && sum < -target || target > 0 && sum < target) {
        return 0;
    }
    
    if ((sum + target) % 2 !== 0) {
        return 0;
    }
    
    let newTarget = (sum + target) / 2;
    
    let dp = new Array(newTarget + 1).fill(0);
    dp[0] = 1;
    
    for (let i = 0; i < nums.length; i++) {
        for (let j = newTarget; j >= nums[i]; j--) {
            dp[j] += dp[j - nums[i]];
        }
    }
    
    return dp[newTarget];
};