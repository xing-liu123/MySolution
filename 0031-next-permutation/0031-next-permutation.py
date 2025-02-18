class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        idx = n - 1

        while idx > 0 and nums[idx - 1] >= nums[idx]:
            idx -= 1

        if idx == 0:
            nums.reverse()
            return 

        
        for j in range(n - 1, idx - 1, -1):
            if nums[j] > nums[idx - 1]:
                nums[idx - 1], nums[j] = nums[j], nums[idx - 1]
                nums[idx:] = reversed(nums[idx:])
                break

            
         

        

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


            

