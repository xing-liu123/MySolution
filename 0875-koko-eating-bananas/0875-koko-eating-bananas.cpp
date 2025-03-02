class Solution {
public:
    bool isEnough(vector<int>& piles, int h, int s) {
        long long time = 0;
        for (int i : piles) {
            if (i % s == 0) {
                time += i / s;
            } else {
                time += (i / s + 1);
            }
        }
        return h >= time;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        if (piles.size() == 1) {
            return (piles[0] + h - 1) / h;
        }


        sort(piles.begin(), piles.end());
        int left = 1;
        int right = piles[piles.size() - 1];
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (isEnough(piles, h, mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};