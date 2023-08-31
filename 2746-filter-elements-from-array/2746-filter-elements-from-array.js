/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const newArr = [];
    for (const i in arr) {
        if (fn(arr[i], Number(i))) {
            newArr.push(arr[i]);
        }
    }
    return newArr;
};