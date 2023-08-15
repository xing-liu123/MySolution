class Solution {
    public int[] plusOne(int[] digits) {
        int i = digits.length - 1;
        digits[i]++;

        while (i >= 0 && digits[i] == 10) {
            digits[i] = 0;
            i--;
            if (i >= 0) {
                digits[i]++;
            } else {
                int[] arr = new int[digits.length + 1];
                arr[0] = 1;
                for (int j = 0; j < digits.length; j++) {
                    arr[j + 1] = digits[j];

                }
                return arr;
            }
            
        }

        return digits;
    }
}