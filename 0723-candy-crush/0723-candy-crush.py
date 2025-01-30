class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        m, n = len(board), len(board[0])

        def check(m, n):
            cellsToUpdate = defaultdict(list)

            for i in range(m):
                last = board[i][0]
                count = 1 if last != 0 else 0
                for j in range(1, n):
                    if board[i][j] == last and last != 0:
                        count += 1
                    else:
                        if count >= 3:
                            cellsToUpdate[i].append((j - count, j - 1))

                        last = board[i][j]
                        count = 1 if last != 0 else 0

                if count >= 3:
                    cellsToUpdate[i].append((n - count, n - 1))

            cellsToUpdate1 = defaultdict(list)

            for j in range(n):
                last = board[0][j]
                count = 1 if last != 0 else 0

                for i in range(1, m):
                    if board[i][j] == last and last != 0:
                        count += 1
                    else:
                        if count >= 3:
                            cellsToUpdate1[j].append((i - count, i - 1))
                        last = board[i][j]
                        count = 1 if last != 0 else 0

                if count >= 3:
                    cellsToUpdate1[j].append((m - count, m - 1))

            return cellsToUpdate, cellsToUpdate1
               
        def update(cellsToUpdate, cellsToUpdate1, m, n):
            for row in cellsToUpdate:
                for cols in cellsToUpdate[row]:
                    left, right = cols

                    for j in range(left, right + 1):
                        board[row][j] = 0

            for col in cellsToUpdate1:
                for rows in cellsToUpdate1[col]:
                    top, bot = rows

                    for i in range(top, bot + 1):
                        board[i][col] = 0

            for j in range(n):
                bot = m - 1

                for top in range(m - 1, -1, -1):
                    if board[top][j] != 0:
                        board[bot][j] = board[top][j]
                        bot -= 1

                for i in range(bot, -1, -1):
                    board[i][j] = 0

        while True:
            cell1, cell2 = check(m, n)

            if len(cell1) + len(cell2) == 0:
                return board

            update(cell1, cell2, m, n)

        return board
