class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        prev1 = nums[0]
        prev2 = nums[1]

        i = 2

        for j in range(2, n):
            if nums[j] != prev1:
                prev1 = prev2
                prev2 = nums[j]
                nums[i] = nums[j]
                i += 1
        
        return i