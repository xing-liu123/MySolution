class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        n = len(board)
        other_color = "W" if color == "B" else "B"

        # up
        if rMove > 1 and board[rMove - 1][cMove] == other_color :
            i = rMove - 2

            while i > 0 and board[i][cMove] == other_color:
                i -= 1
            
            if board[i][cMove] == color:
                return True

        # left
        if cMove > 1 and board[rMove][cMove - 1] == other_color:
            j = cMove - 2

            while j > 0 and board[rMove][j] == other_color:
                j -= 1

            if board[rMove][j] == color:
                return True

        # up left
        if rMove > 1 and cMove > 1 and board[rMove - 1][cMove - 1] == other_color:
            i = rMove - 2
            j = cMove - 2

            while i > 0 and j > 0 and board[i][j] == other_color:
                i -= 1
                j -= 1
            
            if board[i][j] == color:
                return True

        # up right 
        if rMove > 1 and n - cMove >= 3 and board[rMove - 1][cMove + 1] == other_color:
            i = rMove - 2
            j = cMove + 2

            while i > 0 and j < n - 1 and board[i][j] == other_color:
                i -= 1
                j += 1
            
            if board[i][j] == color:
                return True

        # down
        if n - rMove >= 3 and board[rMove + 1][cMove] == other_color:
            i = rMove + 2

            while i < n - 1 and board[i][cMove] == other_color:
                i += 1
            
            if board[i][cMove] == color:
                return True

        # down left
        if n - rMove >= 3 and cMove > 1 and board[rMove + 1][cMove - 1] == other_color:
            i = rMove + 2
            j = cMove - 2
            while i < n - 1 and j > 0 and board[i][j] == other_color:
                i += 1
                j -= 1
            
            if board[i][j] == color:
                return True

        # down right
        if n - rMove >= 3 and n - cMove >= 3 and board[rMove + 1][cMove + 1] == other_color:
            i = rMove + 2
            j = cMove + 2

            while i < n - 1 and j < n - 1 and board[i][j] == other_color:
                i += 1
                j += 1
            
            if board[i][j] == color:
                return True


        # right
        if n - cMove >= 3 and board[rMove][cMove + 1] == other_color:
            j = cMove + 2

            while j < n - 1 and board[rMove][j] == other_color:
                j += 1

            if board[rMove][j] == color:
                return True

        return False
