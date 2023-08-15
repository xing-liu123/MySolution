class Solution {
public:
    bool isValid(string s) {
        stack<char> myStack;

        for (char c : s) {
            if (myStack.empty()) {
                myStack.push(c);
            } else {
                 char cOnTop = myStack.top();

            switch(c) {
               
                case ')':
                    if (cOnTop != '(') {
                        return false;
                    } else {
                        myStack.pop();
                    }
                    break;
                case ']':
                    if (cOnTop != '[') {
                        return false;
                    } else {
                        myStack.pop();
                    }
                    break;
                case '}':
                    if (cOnTop != '{') {
                        return false;
                    } else {
                        myStack.pop();
                    }
                    break;
                default:
                    myStack.push(c);
            }
            }
           
        }
        return myStack.empty();
    }
};