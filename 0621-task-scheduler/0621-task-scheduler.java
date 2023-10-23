class Solution {
    public int leastInterval(char[] tasks, int n) {
        // Map<Character, Integer> freq = new HashMap<>();

        // for (char task : tasks) {
        //     freq.put(task, freq.getOrDefault(task, 0) + 1);
        // }

        // PriorityQueue<Character> pq = new PriorityQueue<>((a, b) -> freq.get(b) - freq.get(a));

        // pq.addAll(freq.keySet());

        // int totalInterval = 0;

        // while (!pq.isEmpty()) {
        //     List<Character> coolDownList = new ArrayList<>();

        //     int interval = 0;

        //     while (interval <= n) {
        //         if (!pq.isEmpty()) {
        //             char c = pq.poll();
        //             freq.put(c, freq.get(c) - 1);

        //             if (freq.get(c) > 0) {
        //                 coolDownList.add(c);
        //             }
        //         }
        //         interval++;
        //         totalInterval++;

        //         if (pq.isEmpty() && coolDownList.isEmpty()) {
        //             return totalInterval;
        //         }
        //     }

        //     pq.addAll(coolDownList);
        // }

        // return totalInterval;

        int[] freq = new int[26];

        for (char c : tasks) {
            freq[c - 'A']++; 
        }

        Arrays.sort(freq);

        int freq_max = freq[freq.length - 1];
        int idle_time = (freq_max - 1) * n;

        for (int i = freq.length - 2; i >= 0 && idle_time > 0; i--) {
            idle_time -= Math.min(freq_max - 1, freq[i]);
        }

        idle_time = Math.max(0, idle_time);

        return idle_time + tasks.length;
    }
}