class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> res(nums.size(), -1);
        deque<int> myDeque;
        myDeque.push_back(0);

        for (int i = 1; i < nums.size() * 2; i++) {
            int idx = i % nums.size();
            if(nums[idx] <= nums[myDeque.back()]) {
                myDeque.push_back(idx);
            } else {
                while(!myDeque.empty() && nums[idx] > nums[myDeque.back()]) {
                    res[myDeque.back()] = nums[idx];
                    myDeque.pop_back();
                }
                myDeque.push_back(idx);
            }
        }
        return res;
    }
};