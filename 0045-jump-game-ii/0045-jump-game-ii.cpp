class Solution {
public:
    int jump(vector<int>& nums) {
        int nextCover = 0;
        int currCover = 0;
        int count = 0;
        for (int i = 0; i < nums.size() - 1; i++) {
            nextCover = max(nextCover, nums[i] + i);
            if (i == currCover) {
                currCover = nextCover;
                count++;
                if (currCover > nums.size() - 1) {
                    return count;
                }
            }
        }

        return count;
        
    }
};