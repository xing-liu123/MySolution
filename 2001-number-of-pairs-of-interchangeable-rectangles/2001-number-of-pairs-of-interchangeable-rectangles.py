class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        rec_counts = defaultdict(lambda: 0)

        for w, h in rectangles:
            rec_counts[(1, h / w)] += 1

        res = 0

        for count in rec_counts.values():
            if count > 1:
                res += math.comb(count, 2)
        
        return res