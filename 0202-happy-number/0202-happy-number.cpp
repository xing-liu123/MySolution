class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> mySet;
        mySet.insert(n);
        while (true) {
            int sum = 0;
            while(n != 0) {
                sum += pow((n % 10), 2);
                n /= 10;
            }

            if (sum == 1) {
                return true;
            }

            n = sum;

            if (mySet.find(n) != mySet.end()) {
                return false;
            }

            mySet.insert(n);
        }

        return true;
    }
};