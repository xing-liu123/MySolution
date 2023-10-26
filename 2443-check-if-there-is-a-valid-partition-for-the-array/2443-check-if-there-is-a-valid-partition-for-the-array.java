class Solution {
    public boolean validPartition(int[] nums) {
       boolean[] dp = new boolean[nums.length + 2];
       dp[0] = true;
       dp[1] = true;
       dp[3] = nums[0] == nums[1];

       for (int i = 4; i < nums.length + 2; i++) {
           if (nums[i - 2] == nums[i - 3]) {
               if (nums[i - 3] == nums[i - 4]) {
                   dp[i] = dp[i - 3] || dp[i - 2];
               } else {
                   dp[i] = dp[i - 2];
               }
           } else if (nums[i - 2] == nums[i - 3] + 1 && nums[i - 3] == nums[i - 4] + 1) {
               dp[i] = dp[i - 3];
           }
       } 

       return dp[nums.length + 1];
    }
}