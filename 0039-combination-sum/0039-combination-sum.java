class Solution {
    List<List<Integer>> res;
    List<Integer> list;
    int sum;
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        res = new ArrayList<>();
        list = new ArrayList<>();
        sum = 0;
        Arrays.sort(candidates);
        backtracking(candidates, 0, target);

        return res;
    }

    private void backtracking(int[] candidates, int start, int target) {
        if (sum == target) {
            res.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (sum + candidates[i] > target) {
                return;
            }
            list.add(candidates[i]);
            sum += candidates[i];
            backtracking(candidates, i, target);
            sum -= candidates[i];
            list.remove(list.size() - 1);
        }
    }

}