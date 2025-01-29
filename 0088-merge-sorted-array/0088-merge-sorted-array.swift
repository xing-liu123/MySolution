class Solution {
    func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
        var idx1 = m
        var idx2 = n

        while idx1 > 0 || idx2 > 0 {
            if idx2 == 0 {
                nums1[idx1 + idx2 - 1] = nums1[idx1 - 1]
                idx1 -= 1
            } else if idx1 == 0 {
                nums1[idx1 + idx2 - 1] = nums2[idx2 - 1]
                idx2 -= 1
            } else if nums1[idx1 - 1] >= nums2[idx2 - 1] {
                nums1[idx1 + idx2 - 1] = nums1[idx1 - 1]
                idx1 -= 1
            } else {
                nums1[idx1 + idx2 - 1] = nums2[idx2 - 1]
                idx2 -= 1
            }
        }

    }
}