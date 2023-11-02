class Solution {
    public int orderOfLargestPlusSign(int n, int[][] mines) {
        int[][] grid = new int[n][n];

        for (int[] row : grid) {
            Arrays.fill(row, 1);
        }

        for (int[] mine : mines) {
            grid[mine[0]][mine[1]] = 0;
        }

        int[][][] dp = new int[n][n][4];

        // left up
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    dp[i][j][0] = j == 0 ? 1 : dp[i][j - 1][0] + 1;
                    dp[i][j][1] = i == 0 ? 1 : dp[i - 1][j][1] + 1;
                }
            }
        }

        int max = 0;

        // right down
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 1) {
                    dp[i][j][2] = j == (n - 1) ? 1 : dp[i][j + 1][2] + 1;
                    dp[i][j][3] = i == (n - 1) ? 1 : dp[i + 1][j][3] + 1;
                }

                int min = Math.min(Math.min(dp[i][j][0], dp[i][j][1]), Math.min(dp[i][j][2], dp[i][j][3]));
                max = Math.max(max, min);
            }
        }

        return max;
    }
}