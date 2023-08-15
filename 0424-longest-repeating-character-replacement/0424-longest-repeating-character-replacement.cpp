class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0;
        vector<int> counts(26, 0);
        int len = 0;
        int maxCount = 0;
        for (int right = 0; right < s.size(); right++) {
            maxCount = max(maxCount, ++counts[s[right] - 'A']);

            while(right - left + 1 - maxCount > k) {
                counts[s[left] - 'A']--;
                left++;
            }

            len = max(len, right - left + 1);
        }

        return len;
    }
};