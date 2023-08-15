class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> mySet;

        int len = 0;

        int left = 0;

        for (int right = 0; right < s.size(); right++) {
            char c = s[right];

            while(mySet.find(c) != mySet.end()) {
                mySet.erase(s[left++]);
            }

            mySet.insert(c);
            len = max(len, right - left + 1);
            
        }

        return len;


    }
};