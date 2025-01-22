/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const newArr = new Array(arr.length);
    // for (const i in arr) {
    //     newArr[i] = fn(arr[i], Number(i));
    // }

    for (let i = 0; i < arr.length; i++) {
        newArr[i] = fn(arr[i], i)
    }
    return newArr;
};