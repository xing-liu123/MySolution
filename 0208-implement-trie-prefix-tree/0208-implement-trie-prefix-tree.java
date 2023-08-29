class Trie {
    private static class TrieNode {
        private TrieNode[] children = new TrieNode[26];
        private boolean isEnd;

        public TrieNode() {
            isEnd = false;
        }
    }

    private final TrieNode root;
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;

        for (char c : word.toCharArray()) {
            if (node.children[c - 'a'] == null) {
                node.children[c - 'a'] = new TrieNode();
            }
            node = node.children[c - 'a'];
        }

        node.isEnd = true;
    }
    
    public boolean search(String word) {
        TrieNode node = root;
        
        for (char c : word.toCharArray()) {
            if (node.children[c - 'a'] != null) {
                node = node.children[c - 'a'];
            } else {
                return false;
            }
        }
        return node.isEnd;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        
        for (char c : prefix.toCharArray()) {
            if (node.children[c - 'a'] != null) {
                node = node.children[c - 'a'];
            } else {
                return false;
            }
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */