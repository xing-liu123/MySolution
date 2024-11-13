class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 1:
            return False

        remainderMap = {}

        currSum = 0

        for i in range(len(nums)):
            currSum += nums[i]

            if i > 0 and currSum == 0:
                return True

            r = currSum % k

            if i > 0 and r == 0:
                return True


            if r in remainderMap and remainderMap[r] < i - 1:
                return True
            
            if not r in remainderMap:
                remainderMap[r] = i

        return False

        

