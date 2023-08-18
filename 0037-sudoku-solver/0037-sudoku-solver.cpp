class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        backtracking(board);
    }

    bool backtracking(vector<vector<char>>& board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col] != '.') {
                    continue;
                }

                for (char c = '1'; c <= '9'; c++) {
                    if (isValid(board, row, col, c)) {
                        board[row][col] = c;
                        if (backtracking(board)) {
                            return true;
                        }
                        board[row][col] = '.';
                    }
                }

                return false;
            }
        }

        return true;
    }

    bool isValid(vector<vector<char>>& board, int row, int col, char c) {
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == c) {
                return false;
            }
        }

        for (int j = 0; j < 9; j++) {
            if (board[row][j] == c) {
                return false;
            }
        }

        for (int i = row / 3 * 3; i < row / 3 * 3 + 3; i++) {
            for (int j = col / 3 * 3; j < col / 3 * 3 + 3; j++) {
                if (board[i][j] == c) {
                    return false;
                }
            }
        }

        return true;
    }
};