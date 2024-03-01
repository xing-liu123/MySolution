/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length == 1) {
        return nums[0];
    }
    
    let x = nums[0];
    let y = Math.max(nums[0], nums[1]);
    
    for (let i = 2; i < nums.length; i++) {
        let z = Math.max(y, x + nums[i]);
        x = y
        y = z;
    }
    
    return y;
};