class Solution {
    int[] dr = new int[]{1, -1, 0, 0};
    int[] dc = new int[]{0, 0, 1, -1};

    public void wallsAndGates(int[][] rooms) {
        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < rooms.length; i++) {
            for (int j = 0; j < rooms[0].length; j++) {
                if (rooms[i][j] == 0) {
                    queue.offer(new int[]{i, j});
                }
            }
        }

        while (!queue.isEmpty()) {
            int size = queue.size();

            while (size > 0) {
                int[] point = queue.poll();
                int row = point[0];
                int col = point[1];

                for (int k = 0; k < 4; k++) {
                    int newRow = row + dr[k];
                    int newCol = col + dc[k];

                    if (newRow >= 0 && newRow < rooms.length && newCol >= 0 && newCol < rooms[0].length && rooms[newRow][newCol] == Integer.MAX_VALUE) {
                        rooms[newRow][newCol] = rooms[row][col] + 1;
                        queue.offer(new int[]{newRow, newCol});
                    }
                }

                size--;                
            }
        }
    }
}