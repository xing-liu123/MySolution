class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> freq = new HashMap<>();

        for (char task : tasks) {
            freq.put(task, freq.getOrDefault(task, 0) + 1);
        }

        PriorityQueue<Character> pq = new PriorityQueue<>((a, b) -> freq.get(b) - freq.get(a));

        pq.addAll(freq.keySet());

        int totalInterval = 0;

        while (!pq.isEmpty()) {
            List<Character> coolDownList = new ArrayList<>();

            int interval = 0;

            while (interval <= n) {
                if (!pq.isEmpty()) {
                    char c = pq.poll();
                    freq.put(c, freq.get(c) - 1);

                    if (freq.get(c) > 0) {
                        coolDownList.add(c);
                    }
                }
                interval++;
                totalInterval++;

                if (pq.isEmpty() && coolDownList.isEmpty()) {
                    return totalInterval;
                }
            }

            pq.addAll(coolDownList);
        }

        return totalInterval;
    }
}