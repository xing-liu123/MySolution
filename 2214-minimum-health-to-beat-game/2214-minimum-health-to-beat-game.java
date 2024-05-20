class Solution {
    public long minimumHealth(int[] damage, int armor) {
        long sum = 0;
        int max = Integer.MIN_VALUE;
        
        for (int d : damage) {
            sum += d;
            max = Math.max(max, d);
        }
        
        return (armor >= max ? sum - max + 1 : sum - armor + 1);
    }
}