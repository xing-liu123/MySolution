class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        dr = [1, 1, 1, 0, 0, -1, -1, -1]
        dc = [-1, 0, 1, 1, -1, -1, 0, 1]
        m, n = len(board), len(board[0])

        for r in range(m):
            for c in range(n):
                live_neighbors = 0

                for d in range(8):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                        live_neighbors += 1

                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1
                else:
                    if live_neighbors == 3:
                        board[r][c] = 2
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1
        