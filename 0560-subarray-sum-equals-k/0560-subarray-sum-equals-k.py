class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSums = [nums[0]]

        for num in nums[1:]:
            preSums.append(num + preSums[-1])


        print(preSums)
        sum_map = defaultdict(lambda: 0)
        sum_map[0] = 1

        count = 0

        for s in preSums:
            count += sum_map[s - k]
            sum_map[s] += 1            

        return count
