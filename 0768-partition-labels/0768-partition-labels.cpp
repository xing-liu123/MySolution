class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> res;

        vector<int> chars(26, 0);

        for (int i = 0; i < s.size(); i++) {
            chars[s[i] - 'a'] = i;
        }

        int last = -1;
        int idx = 0;

        for (int i = 0; i < s.size(); i++) {
            idx = max(idx, chars[s[i] - 'a']);

            if (i == idx) {
                res.push_back(i - last);
                last = i;
            }
        }

        return res;
    }
};