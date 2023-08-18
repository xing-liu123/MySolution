class Solution {
public:
    vector<string> res;
    vector<int> used;
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        sort(tickets.begin(), tickets.end());
        used = vector<int>(tickets.size(), 0);
        res.push_back("JFK");
        backtracking(tickets);
        return res;
    }

    bool backtracking(vector<vector<string>>& tickets) {
        if (res.size() == tickets.size() + 1) {
            return true;
        }

        for (int i = 0; i < tickets.size(); i++) {
            if (tickets[i][0] == res[res.size() - 1] && used[i] == 0) {
                res.push_back(tickets[i][1]);
                used[i] = 1;
                if (backtracking(tickets)) {
                    return true;
                }
                used[i] = 0;
                res.pop_back();
            }
        }

        return false;
    }
};