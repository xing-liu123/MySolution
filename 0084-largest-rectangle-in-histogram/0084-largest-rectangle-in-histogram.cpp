class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        if (heights.size() == 1) {
            return heights[0];
        }

        vector<int> extended(heights.size() + 2, 0);

        for (int i = 0; i < heights.size(); i++) {
            extended[i + 1] = heights[i];
        }

        deque<int> myQueue;

        myQueue.push_back(0);

        int res = 0;
        for (int i = 1; i < extended.size(); i++) {
            if (extended[i] > extended[myQueue.back()]) {
                myQueue.push_back(i);
            } else if (extended[i] == extended[myQueue.back()]) {
                myQueue.pop_back();
                myQueue.push_back(i);
            } else {
                while (extended[myQueue.back()] > extended[i]) {
                    int mid = myQueue.back();
                    myQueue.pop_back();
                    int left = myQueue.back();
                    int h = extended[mid];
                    int w = i - left - 1;
                    int v = h * w;
                    res = max(res, v);
                }
                myQueue.push_back(i);
            }
        }

        return res;
    }
};