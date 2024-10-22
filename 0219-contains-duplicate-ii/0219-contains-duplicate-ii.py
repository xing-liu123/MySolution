class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexMap = {}

        for idx, num in enumerate(nums):
            if not num in indexMap:
                indexMap[num] = idx
            else:
                if idx - indexMap[num] <= k:
                    return True
                else:
                    indexMap[num] = idx

        return False