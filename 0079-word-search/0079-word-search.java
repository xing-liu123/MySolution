class Solution {
    int ROW;
    int COL;

    public boolean exist(char[][] board, String word) {
        ROW = board.length;
        COL = board[0].length;

        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                if (backtracking(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean backtracking(char[][] board, String word, int row, int col, int idx) {
        if (idx == word.length()) {
            return true;
        }

        if (row < 0 || col < 0 || row >= ROW || col >= COL || board[row][col] != word.charAt(idx)) {
            return false;
        }

        char c = board[row][col];

        board[row][col] = '#';

        // up
        if (backtracking(board, word, row - 1, col, idx + 1)) {return true;}

        // down
        if (backtracking(board, word, row + 1, col, idx + 1)) {return true;}

        // left
        if (backtracking(board, word, row, col - 1, idx + 1)) {return true;}

        // right
        if (backtracking(board, word, row, col + 1, idx + 1)) {return true;}
        
        board[row][col] = c;

        return false;
    }
}