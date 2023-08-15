class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currMax = nums[0];
        int max = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            currMax = std::max(nums[i], currMax + nums[i]);
            max = std::max(max, currMax);
        }

        return max;
        
    }
};