class Solution {
    private class Union {
        public int[] group;
        public int[] rank;

        public Union(int size) {
            group = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++) {
                group[i] = i;
            }
        }

        public int find(int node) {
            if (group[node] != node) {
                group[node] = find(group[node]);
            }
            return group[node];
        }

        public boolean union(int node1, int node2) {
            int group1 = find(node1);
            int group2 = find(node2);

            if (group1 == group2) {
                return false;
            }

            // if (rank[group1] > rank[group2]) {
            //     group[group2] = group1;
            // } else if(rank[group1] < rank[group2]) {
            //     group[group1] = group2;
            // } else {
            //     group[group1] = group2;
            //     rank[group2]++;
            // }
            group[group2] = group1;

            return true;


        }
    }
    
    public int minCostConnectPoints(int[][] points) {
        ArrayList<int[]> allEdges = new ArrayList<>();

        for (int i = 0; i < points.length - 1; i++) {
            for (int j = i + 1; j < points.length; j++) {
                int weight = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                allEdges.add(new int[]{weight, i, j});
            }
        }

        Collections.sort(allEdges, (e1, e2) -> e1[0] - e2[0]);

        Union u = new Union(points.length);

        int minCost = 0;
        int edgesUsed = 0;

        for (int i = 0; i < allEdges.size() && edgesUsed < points.length - 1; i++) {
            int node1 = allEdges.get(i)[1];
            int node2 = allEdges.get(i)[2];

            if (u.union(node1, node2)) {
                minCost += allEdges.get(i)[0];
                edgesUsed++;
            }
        }

        return minCost;
    }
}