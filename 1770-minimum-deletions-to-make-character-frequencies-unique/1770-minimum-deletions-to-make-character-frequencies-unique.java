class Solution {
    public int minDeletions(String s) {
        Integer[] frequencies = new Integer[26];
        Arrays.fill(frequencies, 0);

        for (int i = 0; i < s.length(); i++) {
            frequencies[s.charAt(i) - 'a']++;
        }

        Arrays.sort(frequencies, (a, b) -> b - a);

        int count = 0;
        for (int i = 1; i < frequencies.length; i++) {
            if (frequencies[i] == 0) {
                break;
            }
            if (frequencies[i] >= frequencies[i - 1]) {
                if (frequencies[i - 1] == 0) {
                    count += frequencies[i];
                    frequencies[i] = 0;
                } else {
                     count += (frequencies[i] - (frequencies[i - 1] - 1));
                    frequencies[i] = frequencies[i - 1] - 1;
                }
               
            }
        }

        return count;
    }
}