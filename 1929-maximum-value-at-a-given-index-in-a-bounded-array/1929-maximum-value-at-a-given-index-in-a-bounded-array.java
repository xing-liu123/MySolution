class Solution {
    public int maxValue(int n, int index, int maxSum) {
        if (n + 1 > maxSum) {
            return 1;
        }

        int currSum = n + 1;


        int leftTotal = index;
        int rightTotal = n - 1 - index;  
        int left = 0;
        if (leftTotal > 0) {
            left = 1;
        }
        int right = 0;
        if (rightTotal > 0) {
            right = 1;
        }
        int res = 2;

        while (currSum < maxSum) {
            res++;
            currSum += (1 + left + right);

            if (left < leftTotal) {
                 left++;
            }

            if (right < rightTotal) {
                right++;
            }

            if (left == leftTotal && right == rightTotal) {
                break;
            }
            
        }
        
        if (currSum == maxSum) {
            return res;
        } else if (currSum > maxSum) {
            return res - 1;
        }

        return res + (maxSum - currSum) / n; 
    }
}