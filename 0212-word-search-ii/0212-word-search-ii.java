class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        Set<String> set = new HashSet<>();
        int length = 0;
        
        for (String word : words) {
            length = Math.max(length, word.length());
            set.add(word);
        }
        
        boolean[][] used = new boolean[board.length][board[0].length];
        
        Set<String> res = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                backtrack(board, sb, i, j, set, used, length, res);
            }
        }
        
        return new ArrayList<>(res);
    }
    
    private void backtrack(char[][] board, StringBuilder sb, int i , int j, Set<String> set, boolean[][] used, int length, Set<String> res) {
        if (used[i][j]) {
            return;
        }
        
        if (sb.length() == length) {
            return;
        }
        
        sb.append(board[i][j]);
        used[i][j] = true;
        
        if (set.contains(sb.toString())) {
            res.add(sb.toString());
        }
            
        if (i > 0) {
            backtrack(board, sb, i - 1, j, set, used, length, res);
        }
            
        if (i < board.length - 1) {
            backtrack(board, sb, i + 1, j, set, used, length, res);
        }
            
        if (j > 0) {
            backtrack(board, sb, i, j - 1, set, used, length, res);
        }
        
        if (j < board[0].length - 1) {
            backtrack(board, sb, i, j + 1, set, used, length, res);
        }
        
        sb.deleteCharAt(sb.length() - 1);
        used[i][j] = false;
    }
}