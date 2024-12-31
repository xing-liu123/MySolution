class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for left, right in intervals:
            if not res or left > res[-1][1]:
                res.append([left, right])
            else:
                res[-1][1] = max(right, res[-1][1])

        return res

            