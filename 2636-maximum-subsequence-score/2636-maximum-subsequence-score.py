class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combined = [list(pair) for pair in zip(nums1, nums2)]
        combined = sorted(combined, key=lambda x: x[1], reverse=True)

        queue = []

        res = 0
        sum = 0

        for i in range(len(combined)):
            heapq.heappush(queue, combined[i][0])
            sum += combined[i][0]

            if len(queue) > k:
                sum -= heapq.heappop(queue)

            if len(queue) == k:
                res = max(res, sum * combined[i][1])

        return res
            
            