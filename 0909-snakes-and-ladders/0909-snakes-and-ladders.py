class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        dist = n * n

        def getPosition(num):
            row = (num - 1) // n
            col = (num - 1) % n
            if row % 2 == 1:
                col = n - col - 1
            
            row = n - 1 - row
            
            return row, col

        queue = deque([(1, 0)])
        visited = set([1])

        while queue:
            
            num, count = queue.popleft()

            if num == dist:
                return count

            for i in range(1, 7):
                nextNum = num + i

                if nextNum > dist:
                    break

                row, col = getPosition(nextNum)

                if board[row][col] != -1:
                    nextNum = board[row][col]

                if not nextNum in visited:
                    queue.append((nextNum, count + 1))
                    visited.add(nextNum)

        return -1
                
       