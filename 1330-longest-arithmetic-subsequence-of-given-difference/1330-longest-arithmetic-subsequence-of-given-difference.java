class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        int n = arr.length;

        Map<Integer, Integer> map = new HashMap<>();
        map.put(arr[0], 0);

        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        int maxLen = 0;

        for (int j = 1; j < n; j++) {
            if (map.containsKey(arr[j] - difference)) {
                dp[j] = dp[map.get(arr[j] - difference)] + 1;
            }
            map.put(arr[j], j);
            maxLen = Math.max(maxLen, dp[j]);
        }

        return maxLen;
    }
}