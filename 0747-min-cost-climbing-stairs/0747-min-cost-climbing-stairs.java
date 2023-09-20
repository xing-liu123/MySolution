class Solution {
    public int minCostClimbingStairs(int[] cost) {
        if (cost.length == 2) {
            return Math.min(cost[0], cost[1]);
        }

        int[] total = new int[cost.length];
        total[0] = cost[0];
        total[1] = cost[1];

        for (int i = 2; i < total.length; i++) {
            total[i] = cost[i] + Math.min(total[i - 1], total[i - 2]);
        }

        return Math.min(total[total.length - 1], total[total.length - 2]);
    }
}