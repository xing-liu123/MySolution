class Solution {
    class MyDeque{
        Deque<Integer> queue = new LinkedList<>();

        void poll(int num) {
            if(!queue.isEmpty() && queue.peek() == num) {
                queue.poll();
            }
        }

        void add(int num) {
            while(!queue.isEmpty() && num > queue.getLast()){
                queue.removeLast();
            }
            queue.add(num);
        }

        int peek(){
            return queue.peek();
        }
    }

    public int[] maxSlidingWindow(int[] nums, int k) {
        if(nums.length == 1) {
            return nums;
        }

        MyDeque queue = new MyDeque();

        int[] arr = new int[nums.length - k + 1];
        int count = 0;
        for (int i = 0; i < k; i++) {
            queue.add(nums[i]);
        }
        arr[count++] = queue.peek();

        for(int i = k; i < nums.length; i++) {
            queue.poll(nums[i - k]);
            queue.add(nums[i]);
            arr[count++] = queue.peek();
        }
        return arr;
    }
}