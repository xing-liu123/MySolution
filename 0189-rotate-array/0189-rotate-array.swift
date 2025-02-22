class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        let n = nums.count

        if k == 0 || k == n {
            return
        }

        let k = k % n

        nums.reverse()
        nums[0..<k].reverse()
        nums[k..<n].reverse()
        
    }
}