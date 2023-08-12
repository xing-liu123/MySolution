class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> queue = new PriorityQueue<>((p0, p1) -> (p1[0]*p1[0] + p1[1]*p1[1]) -(p0[0]*p0[0] + p0[1]*p0[1]));

        for (int[] point : points) {
          queue.offer(point);
          if (queue.size() > k) {
            queue.poll();
          }
        }

        int[][] res = new int[k][];
        
        int count = 0;
        while (!queue.isEmpty()) {
          res[count++] = queue.poll();
        }

        return res;
    }
}