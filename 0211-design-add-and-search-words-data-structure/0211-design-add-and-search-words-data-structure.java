class WordDictionary {
    private static class TrieNode {
        private boolean isEnd;
        private TrieNode[] children = new TrieNode[26];

        public TrieNode() {
            isEnd = false;
        }
    }
    
    private final TrieNode root;
    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
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
        return search(word, root, 0);
    }

    private boolean search(String word, TrieNode node, int idx) {
        if (idx == word.length()) {
            return node.isEnd;
        }

        char c = word.charAt(idx);

        if (c == '.') {
            for (int i = 0; i < 26; i++) {
                if (node.children[i] != null && search(word, node.children[i], idx+1)) {
                    return true;
                }
            }
            return false;
        } else {
            if (node.children[c - 'a'] == null) {
                return false;
            } else {
                return search(word, node.children[c - 'a'], idx + 1);
            }
        }
    }

    
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */