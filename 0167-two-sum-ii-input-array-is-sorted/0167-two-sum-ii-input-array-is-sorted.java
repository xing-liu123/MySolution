class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 1;
        int j = numbers.length;

        int[] res = new int[2];
        while (i < j) {
            int sum = numbers[i - 1] + numbers[j - 1];
            if (sum > target) {
                j--;
            } else if (sum < target) {
                i++;
            } else {
                res[0] = i;
                res[1] = j;
                break;
            }
        }

        return res;
    }
}