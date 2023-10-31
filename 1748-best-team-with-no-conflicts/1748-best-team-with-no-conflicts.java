class Solution {
    public int bestTeamScore(int[] scores, int[] ages) {
        int n = scores.length;

        int[][] arr = new int[n][2];

        for (int i = 0; i < n; i++) {
            arr[i][0] = scores[i];
            arr[i][1] = ages[i];
        }

        Arrays.sort(arr, (a, b) -> a[1] == b[1] ? a[0] - b[0] : a[1] - b[1]);

        int[] dp = new int[n];
        dp[0] = arr[0][0];
        int max = dp[0];

        for (int i = 1; i < n; i++) {
           dp[i] = arr[i][0];

           for (int j = 0; j < i; j++) {
               if (arr[i][0] >= arr[j][0]) {
                   dp[i] = Math.max(dp[i], dp[j] + arr[i][0]);
               }
           }
           max = Math.max(max, dp[i]);
        }

        return max;

    }
}