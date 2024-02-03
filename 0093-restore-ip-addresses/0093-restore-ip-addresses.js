/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    const res = [];
    
    function backtrack(start, path, dotCount) {
        // When we have placed 3 dots and reached the end of the string
        if (dotCount === 3 ){ 
            if (isValid(start, s.length - 1)) {
                res.push(path + s.substring(start));
            }
            return;
        }
        
        // Try placing a dot in all possible positions
        for (let i = start; i < s.length; i++) {
            if (isValid(start, i)) {
                // Place dot if valid and continue
                backtrack(i + 1, path + s.substring(start, i + 1) + '.', dotCount + 1);
            } else {
                // Break early if not valid to save time
                break;
            }
        }
    }
    
    function isValid(start, end) {
        if (end >= s.length || start > end) return false;
        if (s[start] === '0' && start !== end) return false; // Leading zero
        
        let num = parseInt(s.substring(start, end + 1), 10);
        return num <= 255;
    }
    
    backtrack(0, '', 0);
    return res;
};
