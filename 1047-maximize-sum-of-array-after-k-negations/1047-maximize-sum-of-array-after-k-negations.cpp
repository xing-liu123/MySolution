class Solution {
public:
    static bool cmp(int num1, int num2) {
        return abs(num1) > abs(num2);
    }
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end(), cmp);
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (k > 0) {
                if (i == nums.size() - 1) {
                    if (k % 2 == 0) {
                        sum += nums[i];
                    } else {
                        sum -= nums[i];
                    }
                } else {
                    if (nums[i] < 0) {
                        sum -= nums[i];
                        k--;
                    } else {
                        sum += nums[i];
                    }
                } 
                
            } else {
                sum += nums[i];
            }
        }
                   
        return sum;
    }
};