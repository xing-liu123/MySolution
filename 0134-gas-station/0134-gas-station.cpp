class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int currSum = 0;
        int sum = 0;
        int start = 0;
        for (int i = 0; i < gas.size(); i++) {
            currSum += gas[i] - cost[i];
            sum += gas[i] - cost[i];

            if (currSum < 0) {
                start = (i + 1) % gas.size();
                currSum = 0;
            }
        }

        return sum < 0 ? -1 : start;
    }
};