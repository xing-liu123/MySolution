class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        MOD = 10**9 + 7
        times = math.comb(m * n - 2, k - 2)
        
        def oneDimension(length):
            total = 0
            for i in range(length):
                count = length - 1 - i  # how many numbers after i
                # Sum from 1 to count is count * (count + 1) // 2
                total += count * (count + 1) // 2
            return total
        
        # Calculate total distances in each dimension
        row_dist = oneDimension(n)
        col_dist = oneDimension(m)
        
        # Each distance in row can pair with n positions in column
        # Each distance in column can pair with m positions in row
        total = (row_dist * m * m + col_dist * n * n) % MOD
        
        return (total * times) % MOD
                



         