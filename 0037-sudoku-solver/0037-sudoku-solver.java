class Solution {
    public void solveSudoku(char[][] board) {
        solve(board);
    }

    private boolean solve(char[][] board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col] != '.'){
                    continue;
                }
                for (char k = '1'; k <= '9'; k++) {
                    if (isValid(board, row, col, k)) {
                        board[row][col] = k;
                        if (solve(board)){
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

    private boolean isValid(char[][] board, int row, int col, char k) {
        for(int i = 0; i < 9; i++) {
            if ( board[row][i] == k) {
                return false;
            }
        }

        for(int i = 0; i < 9; i++) {
            if ( board[i][col] == k) {
                return false;
            }
        }

        for (int i = (row / 3) * 3; i < (row / 3) * 3 + 3; i++) {
            for (int j = (col / 3) * 3; j < (col / 3) * 3 + 3; j++) {
                if (board[i][j] == k) {
                    return false;
                }
            }
        }

        return true;

    }
}