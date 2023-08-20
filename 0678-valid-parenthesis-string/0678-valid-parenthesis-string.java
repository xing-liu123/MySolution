class Solution {
    public boolean checkValidString(String s) {
        char[] str = s.toCharArray();
        int count = 0;
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < str.length; i++) {
            char c = str[i];

            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                if (!stack.isEmpty()) {
                    stack.pop();
                } else if (count > 0) {
                    count--;
                } else {
                    return false;
                }
            } else {
                count++;
            }

        }

        if (count < stack.size()) {
            return false;
        }

        int count1 = 0;
        Stack<Character> stack1 = new Stack<>();

        for (int i = str.length - 1; i >= 0; i--) {
            char c = str[i];

            if (c == ')') {
                stack1.push(c);
            } else if (c == '(') {
                if (!stack1.isEmpty()) {
                    stack1.pop();
                } else if (count1 > 0) {
                    count1--;
                } else {
                    return false;
                }
            } else {
                count1++;
            }

        }

        return count1 >= stack1.size();
    }
}