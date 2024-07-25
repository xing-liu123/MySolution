class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        n = len(board)
        other_color = "W" if color == "B" else "B"

        # up
        if rMove > 1:
            i = rMove - 1
            count = 0
            while i > 0 and board[i][cMove] == other_color:
                count += 1
                i -= 1
            
            if board[i][cMove] == color and count >= 1:
                return True

        # left
        if cMove > 1:
            j = cMove - 1
            count = 0
            while j > 0 and board[rMove][j] == other_color:
                count += 1
                j -= 1

            if board[rMove][j] == color and count >= 1:
                return True

        # up left
        if rMove > 1 and cMove > 1:
            i = rMove - 1
            j = cMove - 1
            count = 0
            while i > 0 and j > 0 and board[i][j] == other_color:
                count += 1
                i -= 1
                j -= 1
            
            if board[i][j] == color and count >= 1:
                return True

        # up right 
        if rMove > 1 and n - cMove >= 3:
            i = rMove - 1
            j = cMove + 1
            count = 0
            while i > 0 and j < n - 1 and board[i][j] == other_color:
                count += 1
                i -= 1
                j += 1
            
            if board[i][j] == color and count >= 1:
                return True

        # down
        if n - rMove >= 3:
            i = rMove + 1
            count = 0
            while i < n - 1 and board[i][cMove] == other_color:
                count += 1
                i += 1
            
            if board[i][cMove] == color and count >= 1:
                return True

        # down left
        if n - rMove >= 3 and cMove > 1:
            i = rMove + 1
            j = cMove - 1
            count = 0
            while i < n - 1 and j > 0 and board[i][j] == other_color:
                count += 1
                i += 1
                j -= 1
            
            if board[i][j] == color and count >= 1:
                return True

        # down right
        if n - rMove >= 3 and n - cMove >= 3:
            i = rMove + 1
            j = cMove + 1
            count = 0
            while i < n - 1 and j < n - 1 and board[i][j] == other_color:
                count += 1
                i += 1
                j += 1
            
            if board[i][j] == color and count >= 1:
                return True


        # right
        if n - cMove >= 3:
            j = cMove + 1
            count = 0
            while j < n - 1 and board[rMove][j] == other_color:
                print(j, board[rMove][j])
                count += 1
                j += 1

            if board[rMove][j] == color and count >= 1:
                return True

        return False
