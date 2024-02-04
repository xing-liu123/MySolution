/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    const res = [];
    const subset = [];
    nums.sort((a, b) => a - b);
    
    function backtrack(start) {
        res.push([...subset]);
        
        for (let i = start; i < nums.length; i++) {
            if (i !== start && nums[i] === nums[i - 1]) {
                continue;
            }
            
            subset.push(nums[i]);
            backtrack(i + 1);
            subset.pop();
        }
    }
    
    backtrack(0);
    return res;
};