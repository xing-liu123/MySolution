class Solution {
    public String removeDuplicateLetters(String s) {
        int[] arr = new int[26];
        char[] str = s.toCharArray();

        for (char c : str) {
            arr[c - 'a']++;
        }

        Stack<Character> stack = new Stack<>();

        int[] used = new int[26];

        StringBuilder sb = new StringBuilder();

        for (char c : str) {
            arr[c - 'a']--;

            if (used[c - 'a'] == 1) {
                continue;
            }

            while (!stack.isEmpty() && stack.peek() > c && arr[stack.peek() - 'a'] > 0) {
                used[stack.pop() - 'a'] = 0;
            }

            stack.push(c);
            used[c - 'a'] = 1;
        }

        while(!stack.isEmpty()) {
            sb.insert(0, stack.pop());
        }

        return sb.toString();
    }
}