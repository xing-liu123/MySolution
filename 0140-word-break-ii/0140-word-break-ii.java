class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> set = new HashSet<>();
        for (String word : wordDict) {
            set.add(word);
        }
        
        
        List<String> res = new ArrayList<>();
        List<String> path = new ArrayList<>();
        backtrack(s, 0, path, set, res);
        return res;
    }
    
    private void backtrack(String s, int start, List<String> path, Set<String> set, List<String> res) {
        if (start == s.length()) {
            res.add(String.join(" ", path));
            return;
        }
        
        for (int i = start; i < s.length(); i++) {
            if (set.contains(s.substring(start, i + 1))) {
                path.add(s.substring(start, i + 1));
                backtrack(s, i + 1, path, set, res);
                path.remove(path.size() - 1);
            }
            
        }
    }
}