class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : arr) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<Integer> counts = new ArrayList<Integer>(map.values());
        Collections.sort(counts);

        for (int i = 0; i < counts.size(); i++) {
            k -= counts.get(i);

            if (k < 0) {
                return counts.size() - i;
            } else if (k == 0) {
                return counts.size() - i - 1;
            }
        }

        return 0;
    }
}