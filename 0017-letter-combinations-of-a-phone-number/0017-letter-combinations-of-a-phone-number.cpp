class Solution {
public:
    vector<string> keys = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> res;
    string word;
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0) {
            return res;
        }
        backtracking(digits, 0);
        return res;
    }

    void backtracking(string digits, int start) {
        if (word.size() == digits.size()) {
            string copy = word;
            res.push_back(copy);
            return;
        }

        string key = keys[digits[start] - '2'];

        for (int i = 0; i < key.size(); i++) {
            word += key[i];
            backtracking(digits, start + 1);
            word.erase(word.size() - 1, 1);
        }
    }
};