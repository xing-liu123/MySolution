class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        for r in range(n):
            for c in range(n):
                index = 4 * (r * n + c)

                if grid[r][c] == "/":
                    union(index + 0, index + 3)
                    union(index + 1, index + 2)
                elif grid[r][c] == "\\":
                    union(index + 0, index + 1)
                    union(index + 2, index + 3)
                else:
                    union(index + 0, index + 1)
                    union(index + 1, index + 2)
                    union(index + 2, index + 3)

                # Connect adjacent squares
                if r < n - 1:  # Connect bottom part of current cell to top part of below cell
                    union(index + 2, (index + 4 * n) + 0)
                if c < n - 1:  # Connect right part of current cell to left part of right cell
                    union(index + 1, (index + 4) + 3)

        # Count distinct roots (number of connected components)
        return sum(1 for i in range(4 * n * n) if find(i) == i)