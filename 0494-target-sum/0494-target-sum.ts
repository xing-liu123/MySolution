function findTargetSumWays(nums: number[], target: number): number {
    let sum : number = 0;
    
    nums.forEach(num => sum += num);
    
    if (target < 0 && sum < -target || target > 0 && sum < target) {
        return 0;
    }
    
    if ((target + sum) % 2 !== 0) {
        return 0;
    }
    
    let newTarget = (target + sum) / 2;
    
    let dp : number[] = new Array(newTarget + 1).fill(0);
    
    dp[0] = 1;
    
    for (let i = 0; i < nums.length; i++) {
        for (let j = newTarget; j >= nums[i]; j--) {
            dp[j] += dp[j - nums[i]];
        }
    }
    
    return dp[newTarget];
};