/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const res = [];
    const permutation = [];
    const used = new Array(nums.length).fill(false);
    
    function backtrack() {
        if (permutation.length === nums.length) {
            res.push([...permutation]);
            return;
        }
        
        for (let i = 0; i < nums.length; i++) {
            if (!used[i]) {
                used[i] = true;
                permutation.push(nums[i]);
                backtrack();
                permutation.pop();
                used[i] = false;
            }
        }
    }
    
    backtrack();
    return res;
};