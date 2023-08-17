class Solution {
public:
    vector<vector<string>> res;
    vector<string> list;
    vector<vector<string>> partition(string s) {
        backtracking(s, 0);
        return res;
    }

    void backtracking(string s, int start) {
        if (start >= s.size()) {
            res.push_back(list);
            return;
        }

        for (int i = start; i < s.size(); i++) {
            if (isPalindrome(s, start, i)) {
                list.push_back(s.substr(start, i - start + 1));
            } else {
                continue;
            }

            backtracking(s, i + 1);
            list.pop_back();
        }
    }

    bool isPalindrome(string s, int left, int right) {
        while(left < right) {
            if (s[left] == s[right]) {
                left++;
                right--;
            } else {
                return false;
            }
        }

        return true;
    }
};