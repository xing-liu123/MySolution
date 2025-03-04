class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        oneCount = 0
        maxOneCount = 0

        for num in nums:
            if num == 1:
                oneCount += 1
            else:
                maxOneCount = max(maxOneCount, oneCount)
                oneCount = 0

        return max(oneCount, maxOneCount)
            