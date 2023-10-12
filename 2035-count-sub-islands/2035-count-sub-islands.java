class Solution {
    int count = 0;
    int[] dr = {1, -1, 0, 0};
    int[] dc = {0, 0, 1, -1};
    boolean isSub = true;
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        for (int i = 0; i < grid2.length; i++) {
            for (int j = 0; j < grid2[0].length; j++) {
                if (grid2[i][j] == 1) {
                    isSub = true;
                    dfs(grid1, grid2, i, j);
                    if (isSub) {
                        count++;
                    } else {
                        isSub = true;
                    }
                }
            }
        }

        return count;
    }

    private void dfs(int[][] grid1, int[][] grid2, int i, int j) {
        if (i < 0 || j < 0 || i >= grid2.length || j >= grid2[0].length || grid2[i][j] == 0) {
            return;
        }

        if (grid1[i][j] == 0) {
            isSub = false;
        }

        grid2[i][j] = 0;

        for (int k = 0; k < 4; k++) {
            int ii = i + dr[k];
            int jj = j + dc[k];
            dfs(grid1, grid2, ii, jj);
        }

    }
}