class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        queue = deque([(sr, sc, image[sr][sc])])

        while queue:
            row, col, c = queue.popleft()

            for i in range(4):
                next_row = row + dr[i]
                next_col = col + dc[i]

                if 0 <= next_row < m and 0 <= next_col < n and image[next_row][next_col] == c and image[next_row][next_col] != color:
                    queue.append((next_row, next_col, c))

            image[row][col] = color

        return image