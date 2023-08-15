class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] str = s.toCharArray();

        int len = 0, i = 0;
        Set<Character> set = new HashSet<>();

        for (int j = 0; j < str.length; j++) {
            char c = str[j];
            
            while(set.contains(c)) {
                set.remove(str[i++]);
            }

            set.add(c);
            len = Math.max(len, j - i + 1);
        }

        return len;
    }
}