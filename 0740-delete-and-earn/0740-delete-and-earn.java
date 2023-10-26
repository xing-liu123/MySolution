class Solution {
    public int deleteAndEarn(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int maxNum = 0;

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + num);
            maxNum = Math.max(maxNum, num);
        }

        int[] dp = new int[maxNum + 1];
        dp[1] = map.getOrDefault(1, 0);
        
        for (int i = 2; i < dp.length; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + map.getOrDefault(i, 0));
        }

        return dp[maxNum];

        
    }
}