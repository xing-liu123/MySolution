class Solution {
    public int maxProfit(int[] prices) {
        int[][] dp = new int[prices.length][2];

        dp[0][0] = 0;
        dp[0][1] = -prices[0];

        for (int i = 1; i < prices.length; i++) {
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
            dp[i][1] = Math.max(dp[i - 1][1], -prices[i]);
        }

        return Math.max(dp[prices.length - 1][0], dp[prices.length - 1][1]);


        // int min = Integer.MAX_VALUE;
        // int max = 0;

        // for (int i = 0; i < prices.length; i++) {
        //     if (prices[i] < min) {
        //         min = prices[i];
        //     }

        //     if (prices[i] - min > max) {
        //         max = prices[i] - min;
        //     }
        // }

        // return max;   
    }
}