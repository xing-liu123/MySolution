/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const res = [];
    const subset = [];
    
    function backtrack(start) {
        res.push([...subset]);
        
        for (let i = start; i < nums.length; i++) {
            subset.push(nums[i]);
            backtrack(i + 1);
            subset.pop();
        }
    }
    
    backtrack(0);
    return res;
};