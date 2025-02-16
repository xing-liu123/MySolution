class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)

        # nums.sort()

        # res = []

        # if nums[0] > 0:
        #     return res

        # for i in range(n):
        #     if i > 0 and nums[i - 1] == nums[i]:
        #         continue

        #     left = i + 1
        #     right = n - 1

        #     while left < right:
        #         three_sum = nums[i] + nums[left] + nums[right]

        #         if three_sum > 0:
        #             right -= 1
        #         elif three_sum < 0:
        #             left += 1
        #         else:
        #             res.append([nums[i], nums[left], nums[right]])

        #             while left < right and nums[left] == nums[left + 1]:
        #                 left += 1

        #             while left < right and nums[right] == nums[right - 1]:
        #                 right -= 1

        #             left += 1
        #             right -= 1
        
        # return res

        n = len(nums)

        res = []

        nums.sort()

        if nums[0] > 0:
            return res

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                
                if currSum == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif currSum > 0:
                    right -= 1
                else:
                    left += 1

        return res