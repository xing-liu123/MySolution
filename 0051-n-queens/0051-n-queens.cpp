class Solution {
public:
    vector<vector<string>> res;
    vector<vector<char>> board;
    vector<vector<string>> solveNQueens(int n) {
        for (int i = 0; i < n; i++) {
            vector<char> row(n, '.');
            board.push_back(row);
        }
        backtracking(0, n);
        return res;
    }

    void backtracking(int row, int n) {
        if (row == n) {
            res.push_back(convert(board));
            return;
        }

        for (int i = 0; i < n; i++) {
            if (isValid(row, i, n)) {
                board[row][i] = 'Q';
                backtracking(row + 1, n);
                board[row][i] = '.';
            }
        }

    }

    bool isValid(int row, int col, int n) {
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        for (int i = row, j = col; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        for (int i = row; i >= 0; i--) {
            if (board[i][col] == 'Q') {
                return false;
            }
        }

        return true;
    }

    vector<string> convert(vector<vector<char>>& board) {
        vector<string> list;
        for (vector<char> chars : board) {
            string str(chars.begin(), chars.end());
            list.push_back(str);
        }
        return list;
    }
};