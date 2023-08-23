class Solution {
    public String reorganizeString(String s) {
        HashMap<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }

        PriorityQueue<Character> queue = new PriorityQueue<>((a, b) -> map.get(b) - map.get(a));
        queue.addAll(map.keySet());

        StringBuilder sb = new StringBuilder();
        while (queue.size() > 1) {
            char first = queue.poll();
            char second = queue.poll();
            sb.append(first);
            sb.append(second);

            map.put(first, map.get(first) - 1);
            map.put(second, map.get(second) - 1);
            if (map.get(first) > 0) {
                queue.add(first);
            }

             if (map.get(second) > 0) {
                queue.add(second);
            }
        }

        if (!queue.isEmpty()){
            char c = queue.poll();
            if (map.get(c) > 1) {
                return "";
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}