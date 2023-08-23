/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */

public class Solution extends Relation {
    public int findCelebrity(int n) {
        
        int i = 0;
        int j = n - 1;
        while (j >= 0 ) {
            if (knows(i, j) && (i == j ||!knows(j, i))) {
                i++;
                if (i >= n) {
                    return j;
                }
            } else {
                j--;
                i = 0;
            }
        }

        return -1;
    }
}