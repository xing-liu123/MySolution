class Solution {
    Map<Integer, List<int[]>> adj;
    public int networkDelayTime(int[][] times, int n, int k) {
        adj = new HashMap<>();

        for (int[] time : times) {
            int source = time[0];
            int dest = time[1];
            int dist = time[2];

            adj.putIfAbsent(source, new ArrayList<>());
            adj.get(source).add(new int[]{dest, dist});
        }

        for (int node : adj.keySet()) {
            Collections.sort(adj.get(node), (a, b) -> a[1] - b[1]);
        }

        int[] signalReceiveAt = new int[n + 1];
        Arrays.fill(signalReceiveAt, Integer.MAX_VALUE);

        dfs(signalReceiveAt, k, 0);

        int res = 0;

        for (int i = 1; i <= n; i++) {
            res = Math.max(res, signalReceiveAt[i]);
        }

        return res == Integer.MAX_VALUE ? -1 : res;

    }

    private void dfs(int[] signalReceiveAt, int currNode, int currDist) {
        if (currDist >= signalReceiveAt[currNode]) {
            return;
        }

        signalReceiveAt[currNode] = currDist;

        if (!adj.containsKey(currNode)) {
            return;
        }

        for (int[] pair : adj.get(currNode)) {
            int nextNode = pair[0];
            int newDist = pair[1] + currDist;
            dfs(signalReceiveAt, nextNode, newDist);
        }
    }
}