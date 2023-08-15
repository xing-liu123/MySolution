class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;

        for (int num : nums) {
            if (map.find(num) != map.end()) {
                map[num]++;
            } else {
                map[num] = 1;
            }
        }

        auto compare = [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second > b.second;
        };

        priority_queue<pair<int, int>, vector<pair<int, int>>,  decltype(compare)> myQueue(compare);
        for (const auto& entry : map) {
            myQueue.push(entry);
            if (myQueue.size() > k) {
                myQueue.pop();
            }
        }

        vector<int> res;

        while(!myQueue.empty()) {
            res.push_back(myQueue.top().first);
            myQueue.pop();
        }

        return res;
    }
};