class Solution {
public:
    bool isValid(string s) {
        stack<char> myStack;

        for (char c : s) {
            if (c == '{' || c == '[' || c == '(') {
                myStack.push(c);
            } else {
                if (myStack.empty()) {
                    return false;
                }

                char charOnTop = myStack.top();

                if (charOnTop == '(' && c != ')') {return false;}
                if (charOnTop == '[' && c != ']') {return false;}
                if (charOnTop == '{' && c != '}') {return false;}

                myStack.pop();
            }
        
           
        }
        return myStack.empty();
    }
};