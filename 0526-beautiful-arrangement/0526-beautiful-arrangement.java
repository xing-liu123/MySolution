class Solution {
    int count = 0;
    List<Integer> list = new ArrayList<>();
    int[] used;
    public int countArrangement(int n) {
        used = new int[n + 1];
        backtrack(n);
        return count;
    }

    private void backtrack(int n) {
        if (list.size() == n) {
            count++;
            return;
        }

        for (int i = 1; i <= n; i++) {
            if (used[i] == 0 && ((list.size() + 1) % i == 0|| i % (list.size() + 1) == 0)) {
                list.add(i);
                used[i] = 1;
                backtrack(n);
                used[i] = 0;
                list.remove(list.size() - 1);
            }
        }
    }
}