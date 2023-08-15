class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int low = INT_MAX;

        for (int price : prices) {
            if (price < low) {
                low = price;
            }

            if (price - low > res) {
                res = price - low;
            }
        }

        return res;
        
    }
};