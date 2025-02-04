class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        # For each negative number, track min prefix sum possible if we remove all its occurrences
        min_prefix_after_removal = collections.defaultdict(lambda: 0)
        # Track min prefix sum without removing any numbers
        min_prefix_after_removal[0] = 0
        
        # Track the overall maximum subarray sum possible
        max_subarray = float('-inf')
        # Current running sum
        curr_sum = 0
        # Minimum prefix sum seen (considering all possible number removals)
        min_prefix = 0
        
        for num in nums:
            # Update running sum
            curr_sum += num
            
            # Current best subarray sum possible ends at current position
            # It's current sum minus minimum prefix sum seen before
            max_subarray = max(max_subarray, curr_sum - min_prefix)
            
            # If we see a negative number, consider removing all its occurrences
            if num < 0:
                # Calculate new minimum prefix sum if we remove all occurrences of this number
                # Take minimum of:
                # 1. Previous min prefix if we removed this number + current number
                # 2. Current min prefix without any removals + current number
                min_prefix_after_removal[num] = num + min(
                    min_prefix_after_removal[num],  # Previous min if we removed this number
                    min_prefix_after_removal[0]     # Previous min without removals
                )
                
                # Update overall minimum prefix considering this removal
                min_prefix = min(min_prefix, min_prefix_after_removal[num])
            
            # Save current min prefix sum without removals
            prev_min_prefix = min_prefix_after_removal[0]
            # Update min prefix sum without removals
            min_prefix_after_removal[0] = min(prev_min_prefix, curr_sum)
            # Update overall minimum prefix
            min_prefix = min(min_prefix, prev_min_prefix)
        
        return max_subarray