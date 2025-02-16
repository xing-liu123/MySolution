class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        n = len(nums)

        if n < 4:
            return res

        nums.sort()

        if target > 0 and nums[0] > target:
            return res

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    currSum = nums[i] + nums[j] + nums[left] + nums[right]

                    if currSum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif currSum > target:
                        right -= 1

                    else:
                        left += 1

        return res 


        # res = []

        # if (len(nums) < 4):
        #     return res

        # nums.sort()

        # for i in range(len(nums) - 3):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue; 
        #     for j in range(i + 1, len(nums) - 2):
        #         if j > i + 1 and nums[j] == nums[j - 1]:
        #             continue;
                
        #         left = j + 1
        #         right = len(nums) - 1

        #         while left < right:
        #             sum = nums[i] + nums[j] + nums[left] + nums[right]

        #             if sum > target:
        #                 right -= 1
        #             elif sum < target:
        #                 left += 1
        #             else:
        #                 res.append([nums[i], nums[j], nums[left], nums[right]])

        #                 while left < right and nums[left + 1] == nums[left]:
        #                     left += 1
                        
        #                 while left < right and nums[right - 1] == nums[right]:
        #                     right -= 1
                        
        #                 left += 1
        #                 right -= 1
        
        # return res


