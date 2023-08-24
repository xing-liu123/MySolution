class Solution {
    public int twoCitySchedCost(int[][] costs) {
        Arrays.sort(costs, (a, b) -> Math.abs(b[1] - b[0]) - Math.abs(a[1] - a[0]));
        int n = costs.length;

        int a = 0;
        int b = 0;
        int cost = 0;
        for (int i = 0; i < n; i++) {
            if(costs[i][0] > costs[i][1]) {
                if (b < n / 2) {
                    b++;
                    cost += costs[i][1];
                } else {
                    cost += costs[i][0];
                }
            } else if (costs[i][0] < costs[i][1]) {
                if (a < n / 2) {
                    a++;
                    cost += costs[i][0];
                } else {
                    cost += costs[i][1];
                }
            } else {
                cost += costs[i][0];
            }
        } 

        return cost;
    }
}