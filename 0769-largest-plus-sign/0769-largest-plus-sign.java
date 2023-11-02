class Solution {
    public int orderOfLargestPlusSign(int n, int[][] mines) {
        int[][] grid = new int[n][n];

        for (int[] row : grid) {
            Arrays.fill(row, 1);
        }

        for (int[] mine : mines) {
            grid[mine[0]][mine[1]] = 0;
        }

        int max = mines.length < n * n ? 1 : 0;
       int[][][] dp = new int[n][n][2];

       if (grid[0][0] == 0) {
           dp[0][0][0] = 0;
           dp[0][0][1] = 0;
       } else {
           dp[0][0][0] = 1;
           dp[0][0][1] = 1;
       }

       for (int i = 1; i < n; i++) {
           if (grid[i][0] != 0) {
                dp[i][0][0] = dp[i - 1][0][0] + 1;
                dp[i][0][1] = 1;
           } 
       } 

       for (int i = 1; i < n; i++) {
           if (grid[0][i] != 0) {
                dp[0][i][1] = dp[0][i - 1][1] + 1;
                dp[0][i][0] =  1;
           } 
       } 

       for (int i = 1; i < n; i++) {
           for (int j = 1; j < n; j++) {
               if (grid[i][j] == 0) {
                   dp[i][j][0] = 0;
                   dp[i][j][1] = 0;
               } else {
                   dp[i][j][0] = dp[i - 1][j][0] + 1;
                   dp[i][j][1] = dp[i][j - 1][1] + 1;
               }
           }
       }


       int[][][] dp2 = new int[n][n][2];

       if (grid[n - 1][n - 1] == 0) {
           dp2[n - 1][n - 1][0] = 0;
           dp2[n - 1][n - 1][1] = 0;
       } else {
           dp2[n - 1][n - 1][0] = 1;
           dp2[n - 1][n - 1][1] = 1;
       }

       for (int i = n - 2; i >= 0; i--) {
           if (grid[i][n - 1] != 0) {
               dp2[i][n - 1][0] = dp2[i + 1][n - 1][0] + 1;
                dp2[i][n - 1][1] = 1;
           } 
           
       }

        for (int i = n - 2; i >= 0; i--) {
           if (grid[n - 1][i] != 0) {
               dp2[n - 1][i][0] = 1;
                dp2[n - 1][i][1] = dp2[n - 1][i + 1][1] + 1;
           }
       }


        
       for (int i = n - 2; i >= 0; i--) {
           for (int j = n - 2; j >= 0; j--) {
               if (grid[i][j] == 0) {
                   dp2[i][j][0] = 0;
                   dp2[i][j][1] = 0;
               } else {
                   dp2[i][j][0] = dp2[i + 1][j][0] + 1;
                   dp2[i][j][1] = dp2[i][j + 1][1] + 1;
               }

               max = Math.max(max, Math.min(dp[i][j][0], Math.min(dp[i][j][1], Math.min(dp2[i][j][0], dp2[i][j][1]))));
           }
       }

        return max;
    }
}