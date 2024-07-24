from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        step = 0
        visited = set()
        queue = deque([1])
        visited.add(1)

        while queue:
            size = len(queue)
            step += 1

            for _ in range(size):
                curr = queue.popleft()

                for i in range(1, 7):
                    next_pos = curr + i

                    if next_pos <= n * n:
                        x = (n * n - next_pos) // n
                        y = (
                            n - (n * n - next_pos) % n - 1
                            if (n - x) % 2 != 0
                            else (n * n - next_pos) % n
                        )

                        
                        if board[x][y] != -1:
                            next_pos = board[x][y]

                        # print("curr: ", curr, " next: ", next_pos, " Step: ", step)
                        if next_pos == n * n:
                            return step

                        if not next_pos in visited:
                            queue.append(next_pos)
                            visited.add(next_pos)

        return -1
