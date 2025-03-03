class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        oneZeroDiffIdx = {}
        oneZeroDiffIdx[0] = -1

        oneCount = 0
        maxLength = 0

        for idx, num in enumerate(nums):
            if num == 1:
                oneCount += 1
            
            zeroCount = idx + 1 - oneCount
            diff = oneCount - zeroCount

            if diff in oneZeroDiffIdx:
                maxLength = max(maxLength, idx - oneZeroDiffIdx[diff])
            else:
                oneZeroDiffIdx[diff] = idx
                       
        return maxLength