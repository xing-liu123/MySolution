class Solution {
public:
    bool isAlphanumeric(char c) {
        return ('a' <= c && c<= 'z') || ('A' <= c && c<= 'Z') || ('0' <= c && c<= '9');
    }

    bool isPalindrome(string s) {
        int i = 0;
        int j = s.size();

        while (i < j) {
            while (i < j && !isAlphanumeric(s[i])) {
                i++;
            }

            while (i < j && !isAlphanumeric(s[j])) {
                j--;
            }

            if (i < j) {
                if (tolower(s[i]) == tolower(s[j])) {
                    i++;
                    j--;
                } else {
                    return false;
                }
            }
        }

        return true;
    }
};