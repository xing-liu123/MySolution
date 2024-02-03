/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    const res = [];
    let dotCount = 0;
    
    function backtrack(start) {
        if (dotCount === 3) {
            if (isValid(start, s.length - 1)) {
                res.push(s);
            }
            return;
        }
        
        
        for (let i = start; i < s.length; i++) {
            if (isValid(start, i)) {
                s = s.substring(0, i + 1) + "." + s.substring(i + 1, s.length);
                dotCount += 1;
                backtrack(i + 2);
                dotCount -= 1;
                s = s.substring(0, i + 1) + s.substring(i + 2, s.length);
            } else {
                break;
            }
        }
    }
    
    function isValid(start, end) {
        if (end < start || (s[start] === "0" && start !== end)) {
            return false;
        }
        
        let num = parseInt(s.substring(start, end + 1), 10);
        
        return num <= 255;
    }
    
    backtrack(0);
    return res;
};