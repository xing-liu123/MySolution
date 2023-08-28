class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> myMap;

        for (int i = 0; i < nums1.size(); i++) {
            myMap[nums1[i]] = i;
        }

        vector<int> res(nums1.size(), -1);

        deque<int> myQueue;

        myQueue.push_back(0);

        for (int i = 1; i < nums2.size(); i++) {
            if (nums2[i] <= nums2[myQueue.back()]) {
                myQueue.push_back(i);
            } else {
                while(!myQueue.empty() && nums2[myQueue.back()] < nums2[i] ) {
                    if (myMap.find(nums2[myQueue.back()]) != myMap.end()) {
                        res[myMap[nums2[myQueue.back()]]] = nums2[i];
                       
                    }
                     myQueue.pop_back();
                }
                myQueue.push_back(i);
            }
        }
        return res;
    }
};