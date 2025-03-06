class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        idx1, idx2 = 0, 0
        sum1, sum2 = 0, 0  # Running sums for nums1 and nums2
        total = 0  # Stores the final maximum sum
        
        len1, len2 = len(nums1), len(nums2)
        
        while idx1 < len1 or idx2 < len2:
            if idx1 < len1 and (idx2 == len2 or nums1[idx1] < nums2[idx2]):
                sum1 += nums1[idx1]
                idx1 += 1
            elif idx2 < len2 and (idx1 == len1 or nums2[idx2] < nums1[idx1]):
                sum2 += nums2[idx2]
                idx2 += 1
            else:  # nums1[idx1] == nums2[idx2] (common element)
                total += max(sum1, sum2) + nums1[idx1]  # Pick max path and add common number
                total %= MOD  # Keep within modulo bounds
                
                sum1, sum2 = 0, 0  # Reset sums
                idx1 += 1
                idx2 += 1

        # Add the remaining elements from both paths
        total += max(sum1, sum2)  # Pick max of leftover elements
        total %= MOD  # Ensure modulo constraint

        return total
        

        