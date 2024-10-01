class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            partition1 = (low + high) //2
            partition2 = (m + n + 1) // 2 - partition1

            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            # Left and right boundaries of partition in nums2
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total number of elements is odd
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            # Move search space to the left in nums1
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            # Move search space to the right in nums1
            else:
                low = partition1 + 1


