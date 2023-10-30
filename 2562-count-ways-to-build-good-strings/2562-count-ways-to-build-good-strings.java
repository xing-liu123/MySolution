class Solution {
    public int countGoodStrings(int low, int high, int zero, int one) {
        long[] dp = new long[high + 1];
        dp[0] = 1;
        int mod = (int)(1e9 + 7);

        long count = 0;

        for (int i = 1; i <= high; i++) {
            if (i >= zero) {
                dp[i] += dp[i - zero];
            }

            if (i >= one) {
                dp[i] += dp[i - one];
            }

            dp[i] %= mod;

            if (i >= low) {
                count += dp[i];
                count %= mod;
            }
        }

        return (int)(count);
    }
}