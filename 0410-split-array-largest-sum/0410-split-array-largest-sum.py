class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == 1:
            return sum(nums)

        left = nums[0]
        right = sum(nums[1:])

        def isValid(mid):
            curr = 0
            count = 0

            for i, num in enumerate(nums):
                if num > mid:
                    return False
                if curr + num <= mid:
                    curr += num
                else:
                    count += 1
                    curr = num
            
            return count + 1 <= k

        while left <= right:
            mid = (left + right) // 2

            if isValid(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

        