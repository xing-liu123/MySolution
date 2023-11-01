class Solution {
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length;

        int maxLen = 0;
        HashMap<Integer, Integer>[] dp = new HashMap[n];

        for (int j = 0; j < n; j++) {
            dp[j] = new HashMap<>(); 

            for (int i = 0; i < j; i++) {
                int diff = nums[i] - nums[j];
                dp[j].put(diff, dp[i].getOrDefault(diff, 1) + 1);
                maxLen = Math.max(maxLen, dp[j].get(diff));
            }
        }

        return maxLen;

       
    }
}