function lastStoneWeightII(stones: number[]): number {
    if (stones.length == 1) {
        return stones[0];
    }
    
    let sum: number = 0;
    
    stones.forEach(stone => sum += stone);
    
    let target : number = Math.floor(sum / 2);
    
    let dp : number[] = new Array(target + 1).fill(0);
    
    for (let i = 0; i < stones.length; i++) {
        for (let j = target; j >= stones[i]; j--) {
            dp[j] = Math.max(dp[j], dp[j - stones[i]] + stones[i]);
        }
    }
    
    return sum - 2 * dp[target];
};