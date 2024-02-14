class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        }
        
        int x = 1;
        int y = 2;
        
        for (int i = 3; i <= n; i++) {
            int z = x + y;
            x = y;
            y = z;
            
        }
        
        return y;
    }
}