class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        
        Map<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < order.length(); i++) {
            map.put(order.charAt(i), i);
        }

        for (int i = 0; i < words.length - 1; i++) {
            String s1 = words[i];
            String s2 = words[i + 1];

            for(int j = 0; j < s1.length(); j++) {
                if (j == s2.length()) {
                    return false;
                }

                if (map.get(s1.charAt(j)) < map.get(s2.charAt(j))) {
                    break;
                } else if (map.get(s1.charAt(j)) > map.get(s2.charAt(j))) {
                    return false;
                }
            }
        }

        return true;
    }
}