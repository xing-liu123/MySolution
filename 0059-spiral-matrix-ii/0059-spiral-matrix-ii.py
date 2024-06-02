class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0] * n for _ in range(n)]
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        cur_dir = 0  # Start with moving right
        row, col = 0, 0  # Start at the top-left corner
        
        for num in range(1, n * n + 1):
            matrix[row][col] = num
            
            next_row, next_col = row + directions[cur_dir][0], col + directions[cur_dir][1]
            
            if 0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0:
                row, col = next_row, next_col
            else:
                cur_dir = (cur_dir + 1) % 4
                row, col = row + directions[cur_dir][0], col + directions[cur_dir][1]
        
        return matrix
            
        