class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        exps = []
        i, m = 0, n
        while m:
            if m & 1:
                exps.append(i)   # power is 2**i
            m >>= 1
            i += 1

        ps = [0]
        for e in exps:
            ps.append(ps[-1] + e)

        res = []
        for l, r in queries:
            s = ps[r + 1] - ps[l]          # sum of exponents in [l..r]
            res.append(pow(2, s, MOD))     # 2^s mod MOD
        return res