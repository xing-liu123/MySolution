/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const mySet = new Set();
    let maxLen = 0;
    
    let i = 0;
    
    for (let j = 0; j < s.length; j++) {
        while (mySet.has(s[j])) {
            mySet.delete(s[i++]);
        }
        
        mySet.add(s[j]);
        
        maxLen = Math.max(maxLen, j - i + 1);
    }
    
    return maxLen;
};