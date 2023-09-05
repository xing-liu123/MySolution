class Solution {
    int[][] used;
    int[] dr = new int[]{0, 0, 1, -1};
    int[] dc = new int[]{1, -1, 0, 0};
    public void solve(char[][] board) {
        used = new int[board.length][board[0].length];

        for (int i = 1; i < board.length - 1; i++) {
            dfs(board, i, 0);
            dfs(board, i, board[0].length - 1);
        }

        for (int j = 1; j < board[0].length - 1; j++) {
            dfs(board, 0, j);
            dfs(board, board.length - 1, j);
        }

        for (int i = 1; i < board.length - 1; i++) {
            for (int j = 1; j < board[0].length - 1; j++) {
                if (board[i][j] == 'O' && used[i][j] == 0) {
                    board[i][j] = 'X';
                }
            }
        }


    }

    private void dfs(char[][] board, int row, int col) {
        if (row < 0 || row >= board.length || col < 0 || col >= board[0].length || board[row][col] == 'X' || used[row][col] == 1) {
            return;
        }

        used[row][col] = 1;

        for (int k = 0; k < 4; k++) {
            dfs(board, row + dr[k], col + dc[k]);
        }

    }
}