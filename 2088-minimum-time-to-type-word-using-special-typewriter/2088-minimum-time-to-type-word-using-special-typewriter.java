class Solution {
    public int minTimeToType(String word) {
        int time = 0;
        char currLetter = 'a';

        for (int i = 0; i < word.length(); i++) {
            char nextLetter = word.charAt(i);
            int diff = nextLetter - currLetter;
            if (diff >= 0) {
                time += Math.min(diff, -diff + 26);
            } else {
                time += Math.min(-diff, diff + 26);
            }
            time++;
            currLetter = nextLetter;
            
        }

        return time;
    }
}