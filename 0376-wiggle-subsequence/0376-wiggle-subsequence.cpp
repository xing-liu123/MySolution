class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if (nums.size() == 1) {
            return 1;
        }
        
        int count = 1;
        int diff = 0;
        
        for (int i = 1; i < nums.size(); i++) {
            int currDiff = nums[i] - nums[i - 1];
            if ((currDiff > 0 && diff <= 0) || (currDiff < 0 && diff >= 0)) {
                count++;
                diff = currDiff;
            }
            
        }

        return count;
    }
};