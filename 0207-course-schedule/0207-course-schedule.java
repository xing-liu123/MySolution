class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>(numCourses);

        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] prerequisite : prerequisites) {
            adj.get(prerequisite[1]).add(prerequisite[0]);
        }

        boolean[] visited = new boolean[numCourses];
        boolean[] inStack = new boolean[numCourses];

        for (int i = 0; i < numCourses; i++) {
            if (dfs(i, adj, visited, inStack)) {
                return false;
            }
        }

        return true;

    }

    private boolean dfs(int idx, List<List<Integer>> adj, boolean[] visited, boolean[] inStack) {
        if (inStack[idx]) {
            return true;
        }

        if (visited[idx]) {
            return false;
        }

        visited[idx] = true;
        inStack[idx] = true;

        for (int neighbor : adj.get(idx)) {
            if (dfs(neighbor, adj, visited, inStack)) {
                return true;
            }
        }

        inStack[idx] = false;
        return false;
    }
}