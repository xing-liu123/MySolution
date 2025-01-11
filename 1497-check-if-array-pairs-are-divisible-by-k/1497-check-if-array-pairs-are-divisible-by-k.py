class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_counts = defaultdict(int)

        for num in arr:
            remainder = num % k

            if remainder_counts[(k - remainder) % k] > 0:
                remainder_counts[(k - remainder) % k] -= 1
            else:
                remainder_counts[remainder] += 1

        return sum(remainder_counts.values()) == 0
