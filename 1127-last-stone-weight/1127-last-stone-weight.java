class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> queue = new PriorityQueue<>((a, b) -> b - a);

        for (int stone : stones) {
            queue.add(stone);
        }

        while (queue.size() >= 2) {
            int s1 = queue.poll();
            int s2 = queue.poll();
            if (s1 != s2) {
                queue.add(Math.abs(s1 - s2));
            }
        }

        if (queue.isEmpty()) {
            return 0;
        } else {
            return queue.poll();
        }
    }
}