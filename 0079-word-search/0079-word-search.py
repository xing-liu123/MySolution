class Solution:
    def __init__(self):
        self.ROW = 0
        self.COL = 0
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROW = len(board)
        self.COL = len(board[0])

        for i in range(self.ROW):
            for j in range(self.COL):
                if self.backtracking(board, word, i, j, 0):
                    return True
        
        return False
    
    def backtracking(self, board: List[List[str]], word: str, row: int, col: int, start: int) -> bool:
        if start == len(word):
            return True
            
        if row < 0 or row >= self.ROW or col < 0 or col >= self.COL or board[row][col] != word[start]:
            return False
        
        char = board[row][col]
        board[row][col] = "#"
        # up
        if self.backtracking(board, word, row - 1, col, start + 1):
            return True
        
        # down
        if self.backtracking(board, word, row + 1, col, start + 1):
            return True

        # left
        if self.backtracking(board, word, row, col - 1, start + 1):
            return True
        
        # right
        if self.backtracking(board, word, row, col + 1, start + 1):
            return True

        board[row][col] = char

        return False