class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<int[]>> map = new HashMap<>();

        for (int[] time : times) {
            map.computeIfAbsent(time[0], x -> new ArrayList<>()).add(new int[]{time[1], time[2]});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);


        Map<Integer, Integer> res = new HashMap<>();

        pq.offer(new int[]{k, 0});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int node = curr[0];
            int time = curr[1];

            if (res.containsKey(node)) {
                continue;
            }

            res.put(node, time);

            if (map.containsKey(node)) {
                for (int[] edge : map.get(node)) {
                    int nextNode = edge[0];
                    int newTime = edge[1] + time;
                    pq.offer(new int[]{nextNode, newTime});
                }
                
            }
        }

        int maxTime = Collections.max(res.values());
        return res.size() == n ? maxTime : -1;
    }
}