class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixCount = defaultdict(int)
        prefixCount[0] = 1
        count = 0
        currSum = 0

        for i in range(n):
            currSum += nums[i]

            comple = currSum - k

            count += prefixCount[comple]
            prefixCount[currSum] += 1

        return count

        