/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
    if (nums.length === 1) {
        return false;
    }
    
    if (nums.length === 2) {
        return nums[0] === nums[1];
    }
    
    let sum = 0;
    
    nums.forEach(num => sum += num);
    
    if (sum % 2 !== 0) {
        return false;
    }
    
    let target = sum / 2;
   
    
    const dp = new Array(target + 1).fill(0);
    
    for (let i = 0; i < nums.length; i++) {
        for (let j = target; j >= nums[i]; j--) {
            dp[j] = Math.max(dp[j], dp[j - nums[i]] + nums[i]);   
        }

        if (dp[target] === target) {
            return true;
        }
        
    }
    
    return dp[target] === target;
};