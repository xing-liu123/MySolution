class Solution {
    public int maxEvents(int[][] events) {
        Arrays.sort(events, (a, b) -> a[0] - b[0]);

        PriorityQueue<Integer> queue = new PriorityQueue<>();

        int count = 0, i = 0, n = events.length;
        for (int day = 1; day <= 100000; day++) {
           while(!queue.isEmpty() && queue.peek() < day) {
               queue.poll();
           }

           while (i < n && events[i][0] == day) {
               queue.add(events[i][1]);
               i++;
           }

           if (!queue.isEmpty()) {
               queue.poll();
               count++;
           }

           if (i == n && queue.isEmpty()) {
               break;
           }
        }

        return count;
    }
}