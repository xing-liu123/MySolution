class Solution {
    List<List<String>> res = new ArrayList<>();
    List<String> list = new ArrayList<>();
    public List<List<String>> partition(String s) {
        backtracking(s, 0);
        return res;
    }

    private void backtracking(String s, int start) {
        if (start == s.length()) {
            res.add(new ArrayList<String>(list));
            return;
        }

        for (int i = start; i < s.length(); i++) {
            if (isPalindrome(s, start, i)) {
                list.add(s.substring(start, i + 1));
                backtracking(s, i + 1);
                list.remove(list.size() - 1);

            }

            
            
        }
    }

    private boolean isPalindrome(String s, int start, int end) {
       while (start < end) {
           if (s.charAt(start) != s.charAt(end)) {
               return false;
           }
           start++;
           end--;
       }

       return true;
    }
}