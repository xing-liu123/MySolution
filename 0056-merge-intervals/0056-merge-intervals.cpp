class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        int left = intervals[0][0];
        int right = intervals[0][1];

        vector<vector<int>> res;
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] > right) {
                vector<int> interval = {left, right};
                res.push_back(interval);
                left = intervals[i][0];
                right = intervals[i][1];
            } else {
                right = max(right, intervals[i][1]);
            }
        }

        vector<int> interval = {left, right};
        res.push_back(interval);

        return res;
    }
};