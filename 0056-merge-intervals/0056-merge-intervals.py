class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res
            