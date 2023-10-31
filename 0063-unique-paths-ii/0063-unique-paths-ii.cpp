class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid[0][0] == 1) {
            return 0;
        }

        if (obstacleGrid.size() == 1 && obstacleGrid[0].size() == 1) {
            return 1;
        }

        vector<vector<int>> dp(obstacleGrid.size(), vector<int>(obstacleGrid[0].size(), 0));


        for (size_t i = 1; i < obstacleGrid.size(); i++) {
            if (obstacleGrid[i][0] == 1) {
                break;
            }

            dp[i][0] = 1;
        }

        for (size_t i = 1; i < obstacleGrid[0].size(); i++) {
            if (obstacleGrid[0][i] == 1) {
                break;
            }
            
            dp[0][i] = 1;
        }

        for (size_t i = 1; i < obstacleGrid.size(); i++) {
            for (size_t j = 1; j < obstacleGrid[0].size(); j++) {
                if (obstacleGrid[i][j] == 1) {
                    continue;
                }

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        return dp[obstacleGrid.size() - 1] [obstacleGrid[0].size() - 1];
    }
};