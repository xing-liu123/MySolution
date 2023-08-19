class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : hand) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<Integer> keys = new ArrayList<>(map.keySet());
        Collections.sort(keys);

        int left = 0;
        while (left < keys.size() - groupSize + 1) {
            int count = map.get(keys.get(left));
            int newLeft = left;
            for (int i = left + groupSize - 1; i >= left; i--) {
                int currKey = keys.get(i);

                if(i > left && currKey != keys.get(i - 1) + 1) {
                    return false;
                }

                if (map.get(currKey) < count) {
                    return false;
                } else {
                    map.put(currKey, map.get(currKey) - count);

                    if (map.get(currKey) != 0) {
                        newLeft = i;
                    }
                }
            }

            if (newLeft == left) {
                left += groupSize;
            } else {
                left = newLeft;
            }
        }

        return left == keys.size();
    }
}