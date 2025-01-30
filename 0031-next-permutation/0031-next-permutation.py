class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        i = n - 1

        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            nums.sort()
            return

        idxToSwap = i

        for k in range(i, n):
            if nums[k] > nums[i - 1] and nums[k] <= nums[idxToSwap]:
                idxToSwap = k

        nums[i - 1], nums[idxToSwap] = nums[idxToSwap], nums[i - 1]

        nums[i:] = sorted(nums[i:])



        # n = len(nums)

        # i = n - 2

        # while i >= 0 and nums[i] >= nums[i + 1]:
        #     i -= 1

        # if i >= 0:
        #     j = n - 1

        #     while nums[j] <= nums[i]:
        #         j -= 1
            
        #     nums[i], nums[j] = nums[j], nums[i]

        # left, right = i + 1, n - 1

        # while left < right:
        #     nums[left], nums[right] = nums[right], nums[left]
        #     left += 1
        #     right -= 1


            

