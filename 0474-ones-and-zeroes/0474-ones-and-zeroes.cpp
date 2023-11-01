class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (string str : strs) {
            int countOne = 0;
            int countZero = 0;

            for (char c : str) {
                if (c == '0') {
                    countZero++;
                } else {
                    countOne++;
                }
            }

            for (int i = m; i >= countZero; i--) {
                for (int j = n; j >= countOne; j--) {
                    dp[i][j] = max(dp[i][j], dp[i - countZero][j - countOne] + 1);
                }
            }
        }

        return dp[m][n];
    }
};