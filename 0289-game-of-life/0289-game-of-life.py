class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        dr = [1, 1, 1, 0, 0, -1, -1, -1]
        dc = [1, 0, -1, 1, -1, 1, 0, -1]
        boardCopy = copy.deepcopy(board)
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                surroundingSum = 0
                for k in range(8):
                    x = i + dr[k]
                    y = j + dc[k]

                    if 0 <= x < m and 0 <= y < n:
                        surroundingSum += boardCopy[x][y]

                if board[i][j] == 0:
                    if surroundingSum == 3:
                        board[i][j] = 1
                else:
                    if surroundingSum < 2 or surroundingSum > 3:
                        board[i][j] = 0

        