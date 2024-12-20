class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = n - 1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]

                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left + 1] == nums[left]:
                        left += 1

                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1

                    left += 1
                    right -= 1

        return res
                

        # res = []
        # nums = sorted(nums)

        # for i in range(len(nums)):
        #     if nums[0] > 0:
        #         return res
            
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
            
        #     left = i + 1
        #     right = len(nums) - 1
        #     while left < right:
        #         sum = nums[i] + nums[left] + nums[right]

        #         if sum > 0:
        #             right -= 1
        #         elif sum < 0:
        #             left += 1
        #         else:
        #             res.append([nums[i], nums[left], nums[right]])
        #             while left < right and nums[left + 1] == nums[left]:
        #                 left += 1   
        #             while left < right and nums[right - 1] == nums[right]:
        #                 right -= 1
                    
        #             left += 1
        #             right -= 1
        

        # return res