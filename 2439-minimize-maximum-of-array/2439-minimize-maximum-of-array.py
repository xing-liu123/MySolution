class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = sum(nums)

        lowerBound = math.ceil(totalSum / n)
        upperBound = max(nums)


        def isValid(target):
            res = 0
            for num in reversed(nums):
                if num > target:
                    res += num - target
                elif num < target:
                    if res > 0:
                        res = max(0, res - (target - num))

            return res <= 0


        while lowerBound <= upperBound:
            mid = (lowerBound + upperBound) // 2

            if isValid(mid):
                upperBound = mid - 1
            else:
                lowerBound = mid + 1

        return lowerBound
