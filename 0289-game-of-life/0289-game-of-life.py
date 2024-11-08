class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        dr = [1, 1, 1, 0]
        dc = [1, 0, -1, 1]
        m, n = len(board), len(board[0])

        lastRowCopy = None
        leftValue = 0

        for i in range(m):
            rowCopy = copy.copy(board[i])
            for j in range(n):
                surroundingSum = 0
                for k in range(4):
                    x = i + dr[k]
                    y = j + dc[k]

                    if 0 <= x < m and 0 <= y < n:
                        surroundingSum += board[x][y]

                if lastRowCopy:
                    for col in range(j - 1, j + 2):
                        if 0 <= col < n:
                             surroundingSum += lastRowCopy[col]
                if j != 0:
                    surroundingSum += leftValue
                leftValue = board[i][j]

                if board[i][j] == 0:
                    if surroundingSum == 3:
                        board[i][j] = 1
                else:
                    if surroundingSum < 2 or surroundingSum > 3:
                        board[i][j] = 0

            lastRowCopy = copy.copy(rowCopy)