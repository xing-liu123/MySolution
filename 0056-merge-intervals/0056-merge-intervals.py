class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        left, right = intervals[0]
        res = []

        for l, r in intervals:
            if l > right:
                res.append([left, right])
                left = l
                right = r
            else:
                right = max(r, right)

        res.append([left, right])

        return res