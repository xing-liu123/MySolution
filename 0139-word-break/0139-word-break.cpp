class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size(), false);

        for (int i = 0; i < s.size(); i++) {
            string sub1 = s.substr(0, i + 1);
            for (const string& word : wordDict) {
                if (word == sub1) {
                    dp[i] = true;
                    break;
                }

                if (i >= word.size()) {
                    string sub2 = s.substr(i - word.size() + 1, word.size());
                    if (word == sub2 && dp[i - word.size()]) {
                        dp[i] = true;
                        break;
                    }
                }
            }
        }

        return dp[s.size() - 1];
    }
};