class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<int[]> queue = new PriorityQueue<>((pair1, pair2)->pair1[1]-pair2[1]);
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if(queue.size() < k) {
                queue.offer(new int[]{entry.getKey(), entry.getValue()});
            } else if(entry.getValue() > queue.peek()[1]){
                queue.poll();
                queue.offer(new int[]{entry.getKey(), entry.getValue()});

            }
            
            

        }

        int[] res = new int[k];

        for (int i = 0; i < k; i++) {
            res[i] = queue.poll()[0];
        }
        return res;
    }
}