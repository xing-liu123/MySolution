/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length == 1) {
        return nums[0];
    } else if (nums.length == 2) {
        return Math.max(nums[0], nums[1]);
    }
     
    const rob = (start, end) => {
        let x = nums[start];
        let y = Math.max(nums[start], nums[start + 1]);
        
        for (let i = start + 2; i <= end; i++) {
            let z = Math.max(y, x + nums[i]);
            x = y;
            y = z;
        }
        
        return y;
    }
    
    return Math.max(rob(1, nums.length - 1), rob(0, nums.length - 2));
};