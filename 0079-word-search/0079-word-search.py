class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        def search(row, col, idx):
            if idx == len(word):
                return True

            if not (0 <= row < m and 0 <= col < n) or board[row][col] != word[idx]:
                return False

            board[row][col] = ""

            for k in range(4):
                next_row = row + dr[k]
                next_col = col + dc[k]

                if search(next_row, next_col, idx + 1):
                    return True

            board[row][col] = word[idx]

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and search(i, j, 0):
                    return True

        return False




    #    self.ROW = len(board)
    #     self.COL = len(board[0])

    #     for i in range(self.ROW):
    #         for j in range(self.COL):
    #             if self.backtracking(board, word, i, j, 0):
    #                 return True
        
    #     return False
    
    # def backtracking(self, board: List[List[str]], word: str, row: int, col: int, start: int) -> bool:
    #     if start == len(word):
    #         return True
            
    #     if row < 0 or row >= self.ROW or col < 0 or col >= self.COL or board[row][col] != word[start]:
    #         return False
        
    #     char = board[row][col]
    #     board[row][col] = "#"
    #     # up
    #     if self.backtracking(board, word, row - 1, col, start + 1):
    #         return True
        
    #     # down
    #     if self.backtracking(board, word, row + 1, col, start + 1):
    #         return True

    #     # left
    #     if self.backtracking(board, word, row, col - 1, start + 1):
    #         return True
        
    #     # right
    #     if self.backtracking(board, word, row, col + 1, start + 1):
    #         return True

    #     board[row][col] = char

    #     return False 