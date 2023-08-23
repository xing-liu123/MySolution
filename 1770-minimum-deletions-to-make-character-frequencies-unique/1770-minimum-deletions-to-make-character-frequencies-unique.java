class Solution {
    public int minDeletions(String s) {
        int[] frequencies = new int[26];

        for (int i = 0; i < s.length(); i++) {
            frequencies[s.charAt(i) - 'a']++;
        }

        Set<Integer> set = new HashSet<>();

        int count = 0;

        for (int i : frequencies) {
            while (i > 0 && set.contains(i)) {
                i--;
                count++;
            }

            if (i > 0) {
                set.add(i);
            }
        }

        return count;
    }
}