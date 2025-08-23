class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        res = [0] * len(nums)
        idx = len(nums) - 1

        while left <= right:
            rightSquared = nums[right] * nums[right]
            leftSquared = nums[left] * nums[left]
            if rightSquared >= leftSquared:
                res[idx] = rightSquared
                right -= 1
            else:
                res[idx] = leftSquared
                left += 1
            
            idx -= 1

        return res