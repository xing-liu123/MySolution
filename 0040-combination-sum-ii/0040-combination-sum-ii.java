class Solution {
    List<List<Integer>> res = new ArrayList<>();;
    List<Integer> list = new ArrayList<>();;
    int sum = 0;
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        backtracking(candidates, target, 0);
        return res;
    }

    private void backtracking(int[] candidates, int target, int start) {
        if (sum == target) {
            res.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (sum + candidates[i] > target) {
                break;
            }

            if (i != start && candidates[i] == candidates[i - 1]) {
                continue;
            }
            list.add(candidates[i]);
            sum += candidates[i];
            backtracking(candidates, target, i + 1);
            sum -= candidates[i];
            list.remove(list.size() - 1);
        }
    }

   
    
}