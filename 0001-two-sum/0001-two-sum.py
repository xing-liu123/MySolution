class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for idx, num in enumerate(nums):
            comple = target - num
            if comple in index_map:
                return [idx, index_map[comple]]

            index_map[num] = idx

        return  

