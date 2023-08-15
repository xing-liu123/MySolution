class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        if (cost.size() == 2) {
            return min(cost[0], cost[1]);
        }

        vector<int> res(cost.size(), 0);
        res[0] = cost[0];
        res[1] = cost[1];
        
        for (int i = 2; i < res.size(); i++) {
            res[i] = cost[i] + min(res[i - 1], res[i - 2]);
        }

        return min(res[res.size() - 1], res[res.size() - 2]);
    }
};