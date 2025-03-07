class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> lastSeen = new HashMap();

        int left = 0;
        int maxLength = 0;

        for(int right = 0; right < s.length(); right++) {
            if (lastSeen.containsKey(s.charAt(right)) && left <= lastSeen.get(s.charAt(right))) {
                left = lastSeen.get(s.charAt(right)) + 1;
            } 

            maxLength = Math.max(maxLength, right - left + 1);
            lastSeen.put(s.charAt(right), right);
        }

        return maxLength;
    }
}