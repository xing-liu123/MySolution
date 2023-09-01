class Solution {
    public boolean isValidSudoku(char[][] board) {
        int N = 9;
       HashSet<Character>[] rows = new HashSet[9];
       HashSet<Character>[] cols = new HashSet[9];
       HashSet<Character>[] boxes = new HashSet[9];


       for (int i = 0; i < N; i++) {
           rows[i] = new HashSet<>();
           cols[i] = new HashSet<>();
           boxes[i] = new HashSet<>();
           
       }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                char c = board[i][j];
                if (c !=  '.') {
                    if (!rows[i].add(c) || !cols[j].add(c) || !boxes[i/3*3 + j/3].add(c)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}