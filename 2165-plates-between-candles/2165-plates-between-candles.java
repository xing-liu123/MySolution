class Solution {
    public int[] platesBetweenCandles(String s, int[][] queries) {
        int n = s.length();
        char[] str = s.toCharArray();

        int[] plates = new int[n];
        int[] leftCandle = new int[n];
        int[] rightCandle = new int[n];

        int lastCandleIdx = -1;

        for (int i = 0; i < n; i++) {
            if (str[i] == '|') {
                lastCandleIdx = i;
                plates[i] = i == 0 ? 0 : plates[i - 1];
            } else {
                plates[i] = i == 0 ? 1 : plates[i - 1] + 1;
            }

            leftCandle[i] = lastCandleIdx;
            
        }

        int nextCandleIdx = -1;

        for (int i = n - 1; i >= 0; i--) {
            if (str[i] == '|') {
                nextCandleIdx = i;
            }

            rightCandle[i] = nextCandleIdx;
        }

        int[] res = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int left = queries[i][0];
            int right = queries[i][1];

            int rightIdx = leftCandle[right];
            int leftIdx = rightCandle[left]; 
            
            if (leftIdx != -1 && rightIdx != -1 && leftIdx < rightIdx) {
                res[i] = plates[rightIdx] - (leftIdx == 0 ? 0 : plates[leftIdx]);
            } 

        }

        return res;
    }

}