/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var findSubsequences = function(nums) {
    const res = [];
    const sub = [];
    
    function backtrack(start) {
        if (sub.length > 1) {
            res.push([...sub]);
        }
        
        const mySet = new Set();
        
         for (let i = start; i < nums.length; i++) {
                if (mySet.has(nums[i])) {
                    continue;
                }
             
                if (sub.length === 0 || nums[i] >= sub[sub.length - 1]) {
                    mySet.add(nums[i]);
                    sub.push(nums[i]);
                    backtrack(i + 1);
                    sub.pop();
                }
            }
    }
    
    backtrack(0);
    return res;
};