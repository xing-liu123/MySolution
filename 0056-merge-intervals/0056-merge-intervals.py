class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        for l, r in intervals:
            if not res or l > res[-1][1]:
                res.append([l, r])
            else:
                res[-1][1] = max(res[-1][1], r)

        return res