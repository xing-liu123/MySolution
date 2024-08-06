from collections import defaultdict
import math

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        root = list(range(n))
        size = [1] * n

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                root[rootY] = rootX
                size[rootX] += size[rootY]

        factor_map = defaultdict(list)
        
        for i, num in enumerate(nums):
            if num > 1:
                # Finding all prime factors
                for j in range(2, int(math.sqrt(num)) + 1):
                    if num % j == 0:
                        factor_map[j].append(i)
                        while num % j == 0:
                            num //= j
                if num > 1:  # num itself is a prime
                    factor_map[num].append(i)

        # Step 2: Union numbers with shared factors
        for indices in factor_map.values():
            first = indices[0]
            for index in indices[1:]:
                union(first, index)

        # Step 3: Check if all numbers are connected
        return size[find(0)] == n

# Example usage:
sol = Solution()
nums = [4, 6, 15, 35]
print(sol.canTraverseAllPairs(nums))  # True or False
