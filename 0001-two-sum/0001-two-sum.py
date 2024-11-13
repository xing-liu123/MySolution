class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        for idx, num in enumerate(nums):
            if target - num in indexMap:
                return [idx, indexMap[target - num]]

            indexMap[num] = idx

        return None
