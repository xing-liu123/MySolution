class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIdx = {}

        for idx, num in enumerate(nums):
            comple = target - num

            if comple in numIdx:
                return [numIdx[comple], idx]
            else:
                numIdx[num] = idx