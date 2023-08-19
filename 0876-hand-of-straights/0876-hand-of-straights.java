class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : hand) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<Integer> keys = new ArrayList<>(map.keySet());
        Collections.sort(keys);

        int left = 0;
        int count = 0;
        while (left < keys.size() - groupSize + 1) {
            int num = map.get(keys.get(left));
            int newLeft = left;
            for (int i = left + groupSize - 1; i >= left; i--) {
                if(i > left && keys.get(i) != keys.get(i - 1) + 1) {
                    return false;
                }
                if (map.get(keys.get(i)) < num) {
                    return false;
                } else {
                    map.put(keys.get(i), map.get(keys.get(i)) - num);
                    if (map.get(keys.get(i)) != 0) {
                        newLeft = i;
                    }
                }
            }

            count+=num;
            if (newLeft == left) {
                left += groupSize;
            } else {
                left = newLeft;
            }
        }

        return left == keys.size();
    }
}