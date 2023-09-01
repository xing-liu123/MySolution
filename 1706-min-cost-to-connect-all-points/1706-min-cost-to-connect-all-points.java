class Solution {
    // private static class Union {
    //     public int[] group;
    //     public int[] rank;

    //     public Union(int size) {
    //         group = new int[size];
    //         rank = new int[size];
    //         for (int i = 0; i < size; i++) {
    //             group[i] = i;
    //         }
    //     }

    //     public int find(int node) {
    //         if (group[node] != node) {
    //             group[node] = find(group[node]);
    //         }
    //         return group[node];
    //     }

    //     public boolean union(int node1, int node2) {
    //         int group1 = find(node1);
    //         int group2 = find(node2);

    //         if (group1 == group2) {
    //             return false;
    //         }

    //         if (rank[group1] > rank[group2]) {
    //             group[group2] = group1;
    //         } else if(rank[group1] < rank[group2]) {
    //             group[group1] = group2;
    //         } else {
    //             group[group1] = group2;
    //             rank[group2]++;
    //         }

    //         return true;


    //     }
    // }
    
    public int minCostConnectPoints(int[][] points) {
    //     ArrayList<int[]> allEdges = new ArrayList<>();

    //     for (int i = 0; i < points.length - 1; i++) {
    //         for (int j = i + 1; j < points.length; j++) {
    //             int weight = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
    //             allEdges.add(new int[]{weight, i, j});
    //         }
    //     }

    //     Collections.sort(allEdges, (e1, e2) -> e1[0] - e2[0]);

    //     Union u = new Union(points.length);

    //     int minCost = 0;
    //     int edgesUsed = 0;

    //     for (int i = 0; i < allEdges.size() && edgesUsed < points.length - 1; i++) {
    //         int node1 = allEdges.get(i)[1];
    //         int node2 = allEdges.get(i)[2];

    //         if (u.union(node1, node2)) {
    //             minCost += allEdges.get(i)[0];
    //             edgesUsed++;
    //         }
    //     }

    //     return minCost;
    int n = points.length;

    PriorityQueue<Pair<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> a.getKey() - b.getKey());

    boolean[] isUsed = new boolean[n];

    pq.add(new Pair(0,0));

    int cost = 0;
    int edges = 0;

    while (edges < n) {
        Pair<Integer, Integer> pair = pq.poll();

        int dis = pair.getKey();
        int curr = pair.getValue();

        if (isUsed[curr]) {
            continue;
        }

        isUsed[curr] = true;
        edges++;
        cost += dis;

        for (int i = 0; i < n; i++) {
            if (!isUsed[i]) {
                int weight = Math.abs(points[curr][0] - points[i][0]) + Math.abs(points[curr][1] - points[i][1]);
                pq.add(new Pair(weight, i));
                
            }
        }
    }


    return cost;


    //  int n = points.length;
        
    //     // Min-heap to store minimum weight edge at top.
    //     PriorityQueue<Pair<Integer, Integer>> heap = new PriorityQueue<>((a, b) -> (a.getKey() - b.getKey()));;
        
    //     // Track nodes which are included in MST.
    //     boolean[] inMST = new boolean[n];
        
    //     heap.add(new Pair(0, 0));
    //     int mstCost = 0;
    //     int edgesUsed = 0;
        
    //     while (edgesUsed < n) {
    //         Pair<Integer, Integer> topElement = heap.poll();
            
    //         int weight = topElement.getKey();
    //         int currNode = topElement.getValue();
            
    //         // If node was already included in MST we will discard this edge.
    //         if (inMST[currNode]) {
    //             continue;
    //         }
            
    //         inMST[currNode] = true;
    //         mstCost += weight;
    //         edgesUsed++;
            
    //         for (int nextNode = 0; nextNode < n; ++nextNode) {
    //             // If next node is not in MST, then edge from curr node
    //             // to next node can be pushed in the priority queue.
    //             if (!inMST[nextNode]) {
    //                 int nextWeight = Math.abs(points[currNode][0] - points[nextNode][0]) + 
    //                                  Math.abs(points[currNode][1] - points[nextNode][1]);
        
    //                 heap.add(new Pair(nextWeight, nextNode));
    //             }
    //         }
    //     }
        
    //     return mstCost;
    }
}