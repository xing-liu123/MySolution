class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        powers = []

        i = 0
        while n:
            if n & 1:
                powers.append(1 << i)

            n >>= 1
            i += 1

        for i in range(1, len(powers)):
            powers[i] = (powers[i] * powers[i - 1])

        res = []

        for left, right in queries:
            res.append(powers[right]//(powers[left - 1] if left >= 1 else 1) % MOD)

        return res