from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

        queue = deque([(0, 0)])

        steps = 0
        visited = set()
        visited.add((0, 0))

        while queue:
            size = len(queue)

            for _ in range(size):
                cx, cy = queue.popleft()

                if cx == x and cy == y:
                    return steps

                for move in moves:
                    nx, ny = cx + move[0], cy + move[1]

                    if not (nx, ny) in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            steps += 1

        return