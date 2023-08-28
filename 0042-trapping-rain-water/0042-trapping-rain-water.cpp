class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() <= 2) {
            return 0;
        }

        deque<int> myQueue;
        myQueue.push_back(0);
        
        int res = 0;

        for (int i = 1; i < height.size(); i++) {
            if (height[i] < height[myQueue.back()]) {
                myQueue.push_back(i);
            } else if (height[i] == height[myQueue.back()]) {
                myQueue.pop_back();
                myQueue.push_back(i);
            } else {
                while (!myQueue.empty() && height[i] > height[myQueue.back()]) {
                    int mid = myQueue.back();
                    myQueue.pop_back();
                    
                    if (!myQueue.empty()) {
                        int left = myQueue.back();
                        int h = min(height[i], height[left]) - height[mid];
                        int w = i - left - 1;

                        int v = h * w;
                        if (w > 0) {
                            res += v;
                        }
                        
                    }
                }
                myQueue.push_back(i);
            }   
            
        }

        return res;
    }
};