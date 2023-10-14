class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        if (arr.length < k) {
            return 0;
        }
        
        int sum = 0;
        int count = 0;
        int i = 0;
        for (; i < k; i++) {
            sum += arr[i];
        }

        if (sum / k >= threshold) {
            count++;
        }

        for (; i < arr.length; i++) {
            sum -= arr[i - k];
            sum += arr[i];
            if (sum / k >= threshold) {
                count++;
            }
        }

        return count;

    }
}