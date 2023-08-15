class KthLargest {
    PriorityQueue<Integer> queue;
    int k;
    public KthLargest(int k, int[] nums) {
        this.k = k;
        queue = new PriorityQueue<>();
        for (int num : nums) {
            queue.add(num);
            if (queue.size() > k) {
                queue.remove();
            }
        }
    }
    
    public int add(int val) {
        queue.add(val);
        if (queue.size() > this.k) {
            queue.remove();
        }
        
        return queue.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */