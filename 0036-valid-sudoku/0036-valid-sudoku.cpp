class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<string> my_set;

        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (board[i][j] != '.') {
                    string s = "(" + string(1, board[i][j]) +")";
                    if (my_set.find(to_string(i) + s) == my_set.end() && my_set.find(to_string(i/3) + s + to_string(j/3)) == my_set.end() && my_set.find(s + to_string(j)) == my_set.end()) {
                        my_set.insert(to_string(i) + s);
                        my_set.insert(to_string(i/3) + s + to_string(j/3));
                        my_set.insert(s + to_string(j));
                    } else {
                        return false;
                    }
                }
            }
        }

        return true;
    }
};