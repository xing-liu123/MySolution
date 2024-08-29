class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diffMap = {}
        diffMap[0] = -1

        zeroCount, oneCount = 0, 0
        res = 0

        for i, n in enumerate(nums):
            if n == 0:
                zeroCount += 1
            else:
                oneCount += 1
            
            if not oneCount - zeroCount in diffMap:
                diffMap[oneCount - zeroCount] = i
            
            else:
                res = max(res, i - diffMap[oneCount - zeroCount]) 

        return res

