class Solution {
    public int numIslands(char[][] grid) {

        int count = 0;
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    
                    count++;
                    grid[i][j] = '0';

                    Queue<int[]> queue = new LinkedList<>();
                    queue.offer(new int[]{i, j});
                    while (!queue.isEmpty()) {
                        int[] point = queue.poll();

                        int row = point[0];
                        int col = point[1];

                        for (int k = 0; k < 4; k++) {
                            int newRow = row + dr[k];
                            int newCol = col + dc[k];

                            if (newRow >= 0 && newRow < grid.length && newCol >= 0 && newCol < grid[0].length && grid[newRow][newCol] == '1') {
                                queue.offer(new int[]{newRow, newCol});
                                grid[newRow][newCol] = '0';
                            }
                            
                        }
                    }
                }
                
            }
        }

        return count;
    }
}