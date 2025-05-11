class Solution {
    func sortedSquares(_ nums: [Int]) -> [Int] {
        var res = [Int](repeating: 0, count: nums.count)

        var idx = nums.count - 1
        var left = 0
        var right = nums.count - 1

        while left <= right {
            let val1 = nums[left] * nums[left]
            let val2 = nums[right] * nums[right]

            if val1 >= val2 {
                res[idx] = val1
                left += 1
            } else {
                res[idx] = val2
                right -= 1
            }

            idx -= 1
        }

        return res
        

        return res
    }
}