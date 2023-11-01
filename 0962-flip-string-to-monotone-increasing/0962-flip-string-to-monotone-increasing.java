class Solution {
    public int minFlipsMonoIncr(String s) {
        char[] str = s.toCharArray();

        int[][] dp = new int[str.length + 1][2];
        

        for (int i = 1; i <= str.length; i++) {
            if (str[i - 1] == '1') {
                dp[i][0] = dp[i - 1][0] + 1;
                dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][1]);
            } else {
                dp[i][0] = dp[i - 1][0];
                dp[i][1] = dp[i - 1][1] + 1;
            }
        }

        return Math.min(dp[str.length][0], dp[str.length][1]);
    }
}