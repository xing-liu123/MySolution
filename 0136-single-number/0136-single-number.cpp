class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int mask = 0;
        for (int num : nums) {
            mask ^= num;
        }

        return mask;
    }
};