class Solution {
    int[][] used;
    Queue<int[]> queue;
    public int orangesRotting(int[][] grid) {
        used = new int[grid.length][grid[0].length];
        queue = new LinkedList<>();
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                } else if (grid[i][j] == 1) {
                    count++;
                }
            }
        }

        if (count == 0) {
            return 0;
        }

        if (queue.isEmpty()) {
            return -1;
        }

        int res = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();

            boolean roted = false;

            while (size > 0) {
                int[] point = queue.poll();
                int x = point[0];
                int y = point[1];
                
                if (x + 1 < grid.length && used[x + 1][y] == 0 && grid[x + 1][y] == 1) {
                    queue.offer(new int[]{x + 1, y});
                    count--;
                    used[x + 1][y] = 1;
                    roted = true;
                }

                if (x - 1 >= 0 && used[x - 1][y] == 0 && grid[x - 1][y] == 1) {
                    queue.offer(new int[]{x - 1, y});
                    count--;
                    used[x - 1][y] = 1;
                    roted = true;
                }

                if (y + 1 < grid[0].length && used[x][y + 1] == 0 && grid[x][y + 1] == 1) {
                    queue.offer(new int[]{x, y + 1});
                    count--;
                    used[x][y + 1] = 1;
                    roted = true;
                }

                if (y - 1 >= 0 && used[x][y - 1] == 0 && grid[x][y - 1] == 1) {
                    queue.offer(new int[]{x, y - 1});
                    count--;
                    used[x][y - 1] = 1;
                    roted = true;
                }

                size--;
            }

            if (roted) {
                res++;
            }
        }

        return count == 0 ? res : -1;
    }
}