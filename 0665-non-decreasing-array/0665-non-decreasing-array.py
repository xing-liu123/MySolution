class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        isUsed = False

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if not isUsed:
                    if i == 0:
                        nums[i] = nums[i + 1]
                    elif nums[i - 1] <= nums[i + 1]:
                        nums[i] = nums[i - 1]
                    else:
                        nums[i + 1] = nums[i]
                    isUsed = True

                else:
                    return False
        
        return True