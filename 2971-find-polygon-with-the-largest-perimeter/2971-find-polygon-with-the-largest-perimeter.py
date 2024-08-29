class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        otherSum = sum(nums[1: 3])
        res = otherSum + nums[0] if nums[0] < otherSum else -1
        left = 0

        for right in range(3, len(nums)):
            otherSum += nums[right]
            while left + 1 < right and otherSum < nums[left]:
                left += 1
                otherSum -= nums[left]

            if otherSum > nums[left]:
                res = max(res, nums[left] + otherSum)
            
        return res



            