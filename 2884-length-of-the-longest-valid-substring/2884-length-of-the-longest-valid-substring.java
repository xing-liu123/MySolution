class Solution {
    public int longestValidSubstring(String word, List<String> forbidden) {
        Set<String> forbiddenSet = new HashSet<>(forbidden);

        int left = 0;
        int maxLen = 0;
        
        for (int right = 0; right < word.length(); right++) {
            if (forbiddenSet.contains(String.valueOf(word.charAt(right)))) {
                left = right + 1;
                continue;
            } 

            for (int i = Math.max(left, right - 10); i < right; i++) {
                if (forbiddenSet.contains(word.substring(i, right + 1))) {
                    left = i + 1;
                }
            }
            
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
    
}