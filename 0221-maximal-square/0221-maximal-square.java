class Solution {
    public int maximalSquare(char[][] matrix) {
        int[][] dp = new int[matrix.length][matrix[0].length];

        int res = 0;
        for (int j = 0; j < matrix[0].length; j++) {
            if (matrix[0][j] == '1') {
                dp[0][j] = 1;
                res = Math.max(res, dp[0][j]);
            }
            
            
        }

        for (int i = 1; i < matrix.length; i++) {
            if (matrix[i][0] == '1') {
                dp[i][0] = 1;
                res = Math.max(res, dp[i][0]);
            }
        }

        
        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                if (matrix[i][j] == '0') {
                    dp[i][j] = 0;
                } else {
                    int min = Math.min(dp[i - 1][j], Math.min(dp[i - 1][j - 1], dp[i][j - 1]));
                    dp[i][j] = min + 1;
                    
                    res = Math.max(res, dp[i][j]);
                }
            }
        }

        return res * res;
    }
}