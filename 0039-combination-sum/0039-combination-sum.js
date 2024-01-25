/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const path = [];
    const res = [];
    let sum = 0;
    candidates.sort((a, b) => a - b);
    
    function backtrack(start) {
        if (sum == target) {
            res.push([...path]);
            return;
        }
        
        for (let i = start; i < candidates.length; i++) {
            if (sum + candidates[i] > target) {
                return;
            }
            
            path.push(candidates[i]);
            sum += candidates[i];
            backtrack(i);
            path.pop();
            sum -= candidates[i];
        }
    }
    
    backtrack(0);
    return res;
};