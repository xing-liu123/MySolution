/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    const res = [];
    const substrings = [];
    
    function backtrack(start) {
        if (start === s.length) {
            res.push([...substrings]);
        }
        
        for (let i = start; i < s.length; i++) {
            if (isValid(start, i)) {
                substrings.push(s.substring(start, i + 1));
                backtrack(i + 1);
                substrings.pop();
                
            }
        }
    }
    
    function isValid(start, end) {
        if (end < start) {
            return false;
        } else if (end == start) {
            return true;
        } else {
            while (start < end) {
                if (s[start] !== s[end]) {
                    return false;
                }
                start++;
                end--;
            }
            
            return true;
        }
    }
    
    backtrack(0);
    return res;
};