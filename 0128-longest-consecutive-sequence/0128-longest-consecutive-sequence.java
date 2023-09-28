class Solution {
    
    class Union {
        Map<Integer, Integer> parent;
        Map<Integer, Integer> rank;
        int maxSize;

        public Union() {
            parent = new HashMap<>();
            rank = new HashMap<>();
            maxSize = 1;
        }

        private int find(int num) {
            if (parent.get(num) != num) {
                parent.put(num, find(parent.get(num)));
            }
            return parent.get(num); 
        }

        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);

            if (rootX != rootY) {
                int rankX = rank.get(rootX);
                int rankY = rank.get(rootY);

                if (rankX > rankY) {
                    parent.put(rootY, rootX);
                    rank.put(rootX, rankX + rankY);
                    maxSize = Math.max(maxSize, rank.get(rootX));
                } else {
                    parent.put(rootX, rootY);
                    rank.put(rootY, rankX + rankY);
                    maxSize = Math.max(maxSize, rank.get(rootY));
                }
            }
        }

        public void add(int x) {
            parent.put(x, x);
            rank.put(x, 1);
        }

        public boolean contains(int x) {
            return parent.containsKey(x);
        }
        

        public int getMax() {
            return maxSize;
        }
    }


    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        Union u = new Union();
        for (int num : nums) {
            if (!u.contains(num)) {
                u.add(num);
                
            } 
        }

        for (int num : nums) {
            if (u.contains(num + 1)) {
                u.union(num, num + 1);
            }
        }

        return u.getMax();
    }
}