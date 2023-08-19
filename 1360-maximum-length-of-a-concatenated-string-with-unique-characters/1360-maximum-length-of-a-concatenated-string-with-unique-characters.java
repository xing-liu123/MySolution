class Solution {
    int len = 0;
    int[] chars = new int[26];
    int longest = 0;
    HashSet<Character> set = new HashSet<>();
    public int maxLength(List<String> arr) {
        backtrack(arr, 0);
        return longest;
    }

    private void backtrack(List<String> arr, int idx) {
        if (len > longest) {
            longest = len;
        }
        if (idx == arr.size()) {
            
            return;
        }

        for (int i = idx; i < arr.size(); i++) {
            String s = arr.get(i);
            if (!contains(s) && !duplicate(s)) {
                for (int j = 0; j < s.length(); j++) {
                    chars[s.charAt(j) - 'a']++;
                }
                len += s.length();
                backtrack(arr, i + 1);
                len -= s.length();
                for (int j = 0; j < s.length(); j++) {
                    chars[s.charAt(j) - 'a']--;
                }
            }
        }
    }

    private boolean contains(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (chars[s.charAt(i) - 'a'] > 0) {
                return true;
            }
        }

        return false;
    }

    private boolean duplicate(String s) {
         char[] str = s.toCharArray();
         for(char c : str) {
             if (!set.add(c)) {
                 set.clear();
                 return true;
             }
         }

        set.clear();
        return false;

    }
}