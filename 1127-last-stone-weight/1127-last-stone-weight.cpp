class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> myQueue;

        for (int stone : stones) {
            myQueue.push(stone);
        }

        while (myQueue.size() >= 2) {
            int s1 = myQueue.top();
            myQueue.pop();
            int s2 = myQueue.top();
            myQueue.pop();

            if(s1 != s2) {
                 myQueue.push(abs(s1 - s2));
            }
        }

        if (myQueue.empty()) {
            return 0;
        } else {
            return myQueue.top();
        }
    }
};