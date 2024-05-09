/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map();
    const res = [];
    
    for (let i = 0; i < nums.length; i++) {
        if (map.has(target - nums[i])) {
            res[0] = i;
            res[1] = map.get(target - nums[i]);
            break;
        }
        
        map.set(nums[i], i);
    }
    
    return res;
};