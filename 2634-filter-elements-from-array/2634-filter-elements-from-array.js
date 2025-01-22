/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const newArr = [];
    for (const [i, val] of arr.entries()) {
        if (fn(val, i)) {
            newArr.push(val);
        }
    }
    return newArr;
};