class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
    
        def isValid(div):

            return sum((num - 1) // div + 1 for num in nums) <= threshold

        left, right = 1, max(nums)

        while left <= right:
            mid = (left + right) // 2

            if isValid(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
            

