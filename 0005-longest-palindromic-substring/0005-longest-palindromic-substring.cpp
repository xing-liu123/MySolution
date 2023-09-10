class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));

        int left = 0;
        int len = 1;
        for (int i = 0; i < n; i++) {
            for (int j = i; j >= 0; j--) {
                if (s[j] == s[i]) {
                    if (i - j <= 1 || dp[j + 1][i - 1]) {
                        dp[j][i] = true;
                        if (i - j + 1 > len) {
                            len = i - j + 1;
                            left = j;
                        }
                    }
                }
            }
        }

        return s.substr(left, len);
    }
};