class Solution {
public:

    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> my_queue;

        vector<bool> isUsed(n);

        my_queue.push({0, 0});
        int cost = 0;
        int edgesUsed = 0;

        while (edgesUsed < n) {
            pair<int, int> topPair = my_queue.top();
            my_queue.pop();

            int weight = topPair.first;
            int curr = topPair.second;

            if (isUsed[curr]) {
                continue;
            }

            isUsed[curr] = true;
            edgesUsed++;
            cost += weight;

            for (int i = 0; i < n; i++) {
                if (!isUsed[i]) {
                    int nextWeight = abs(points[i][0] - points[curr][0]) + abs(points[i][1] - points[curr][1]);
                    my_queue.push({nextWeight, i});
                }
            }

            
        }  

        return cost;
    }
};