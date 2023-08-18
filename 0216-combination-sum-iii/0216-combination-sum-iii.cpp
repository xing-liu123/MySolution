class Solution {
public:
    vector<vector<int>> res;
    vector<int> list;
    int sum;
    vector<vector<int>> combinationSum3(int k, int n) {
        backtracking(1, n, k);
        return res;
    }

    void backtracking(int start, int n, int k) {
        if (list.size() == k) {
            if (sum == n) {
                vector<int> copy = list;
                res.push_back(copy);
            }
            
            return;
        }

        for (int i = start; i <= 9; i++) {
            if (sum + i > n) {
                continue;
            }

            list.push_back(i);
            sum += i;
            backtracking(i + 1, n, k);
            sum -= i;
            list.pop_back();
        }
    }
};