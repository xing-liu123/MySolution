class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        deque<int> myDeque;
        myDeque.push_back(0);
        vector<int> res(temperatures.size(), 0);

        for (int i = 1; i < temperatures.size(); i++) {
            if (temperatures[i] <= temperatures[myDeque.back()]) {
                myDeque.push_back(i);
            } else {
                while(!myDeque.empty() && temperatures[myDeque.back()] < temperatures[i]) {
                    res[myDeque.back()] = (i - myDeque.back());
                    myDeque.pop_back();
                }
                myDeque.push_back(i);
            }
        }

        return res;
    }
};