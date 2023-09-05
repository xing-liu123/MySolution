class Solution {
    int[][] pacific;
    int[][] atlantic;
    int[] dr = new int[]{1, -1, 0, 0};
    int[] dc = new int[]{0, 0, 1, -1};

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        pacific = new int[heights.length][heights[0].length];
        atlantic = new int[heights.length][heights[0].length];

        for (int i = 0; i < heights.length; i++) {
            dfs(heights, pacific, i, 0);
        }

        for (int i = 0; i < heights.length; i++) {
            dfs(heights, atlantic, i, heights[0].length - 1);
        }

        for (int j = 0; j < heights[0].length; j++) {
            dfs(heights, pacific, 0, j);
        }

        for (int j = 0; j < heights[0].length; j++) {
            dfs(heights, atlantic, heights.length - 1, j);
        }

        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < heights.length; i++) {
            for (int j = 0; j < heights[0].length; j++) {
                if (pacific[i][j] == 1 && atlantic[i][j] == 1) {
                    Integer[] point = new Integer[]{i, j};
                    res.add(Arrays.asList(point));
                }
            }
        }

        return res;
       
    }

    private void dfs(int[][] heights, int[][] used, int row, int col) {
        if (used[row][col] == 1) {
            return;
        }

        used[row][col] = 1;

        for (int k = 0; k < 4; k++) {
            int newRow = row + dr[k];
            int newCol = col + dc[k];

            if (newRow >= 0 && newRow < heights.length && newCol >= 0 && newCol < heights[0].length && heights[newRow][newCol] >= heights[row][col]) {
                dfs(heights, used, newRow, newCol);
            }
        }
    }
}