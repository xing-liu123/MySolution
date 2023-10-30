class Solution {
    public int maxSumMinProduct(int[] nums) {
        int n = nums.length;
        long mod = (long)1e9 + 7;

        long[] prefixSum = new long[n + 1];

        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }

        int[] left = new int[n];
        int[] right = new int[n];

        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop();
            }

            left[i] = stack.isEmpty() ? 0 : stack.peek() + 1;
            stack.push(i);
        }

        stack.clear();

        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop();
            }

            right[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }

        long res = 0;

        for (int i = 0; i < n; i++) {
            long sum = prefixSum[right[i]] - prefixSum[left[i]];
            res = Math.max(res, sum * nums[i]);
        }


        return (int)(res % mod);
    }
}