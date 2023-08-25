class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> counts(n, 1);

        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                counts[i] = counts[i - 1] + 1;
            }
        }

        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                counts[i] = max(counts[i], counts[i + 1] + 1);
            }
        }

        int sum = 0;

        for (int count : counts) {
            sum += count;
        }

        return sum;
    }
};