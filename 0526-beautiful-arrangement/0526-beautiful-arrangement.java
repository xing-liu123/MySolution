class Solution {
    int count = 0;
    List<Integer> list = new ArrayList<>();
    int[] used;
    public int countArrangement(int n) {
        used = new int[n + 1];
        backtrack(1, n);
        return count;
    }

    private void backtrack(int idx, int n) {
        if (idx > n) {
            count++;
            return;
        }

        for (int i = 1; i <= n; i++) {
            if (used[i] == 0 && (idx % i == 0|| i % idx == 0)) {
                list.add(i);
                used[i] = 1;
                backtrack(idx + 1, n);
                used[i] = 0;
                list.remove(list.size() - 1);
            } 
        }
    }
}