class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixCount = defaultdict(int)
        prefixCount[0] = 1
        count = 0

        for i in range(n):
            if i > 0:
                nums[i] += nums[i - 1]

            comple = nums[i] - k

            count += prefixCount[comple]
            prefixCount[nums[i]] += 1

        return count

        