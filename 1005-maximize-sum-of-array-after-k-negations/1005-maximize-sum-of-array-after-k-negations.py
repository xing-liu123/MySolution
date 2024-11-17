class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        if nums[0] > 0:
            if k % 2 == 0:
                return sum(nums)
            else:
                return sum(nums[1:]) - nums[0]

        if nums[-1] < 0 and k >= len(nums):
            if k - len(nums) == 0:
                return -sum(nums)
            else:
                return -sum(nums[:-1]) + nums[-1] 

        for idx, num in enumerate(nums):
            if k > 0:
                if num < 0:               
                    nums[idx] = -nums[idx]
                    k -= 1
                elif num == 0:
                    break
                else:
                    if k % 2 == 0:
                        break
                    else:
                        if num > nums[idx - 1]:
                            nums[idx - 1] = -nums[idx - 1]
                        else:
                            nums[idx] = -nums[idx]
                        
                        break

        

        return sum(nums)