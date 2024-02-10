class Solution {
    private class TrieNode  {
        TrieNode[] children = new TrieNode[26];
        String word = null;
    }
    
    private TrieNode buildNode(String[] words) {
        TrieNode root = new TrieNode();
        
        for (String word : words) {
            TrieNode node = root;
            
            for (char c : word.toCharArray()) {
                if (node.children[c - 'a'] == null) {
                    node.children[c - 'a'] = new TrieNode();
                }
                
                node = node.children[c - 'a'];
            }
            node.word = word;
        }
        
        return root;
    }
    
    public List<String> findWords(char[][] board, String[] words) {
       TrieNode root = buildNode(words);
        
        Set<String> res = new HashSet<>();
        
        boolean[][] visited = new boolean[board.length][board[0].length];
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                dfs(board, i, j, root, visited, res);
            }
        }
        
        return new ArrayList<>(res);
    }
    
    private void dfs(char[][] board, int i, int j, TrieNode root, boolean[][] visited, Set<String> res) {
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || visited[i][j]) return;
        
        char c = board[i][j];
        TrieNode node = root.children[c - 'a'];
        
        if (node == null) {
            return;
        }
        
        visited[i][j] = true;
        
        if (node.word != null) {
            res.add(node.word);
        }
        
        dfs(board, i + 1, j, node, visited, res);
        dfs(board, i - 1, j, node, visited, res);
        dfs(board, i, j + 1, node, visited, res);
        dfs(board, i, j - 1, node, visited, res);
        
        visited[i][j] = false;
    }
    
   
}