class Solution {
    List<List<Integer>> res;
    List<Integer> path;
    public List<List<Integer>> subsets(int[] nums) {
        res = new ArrayList<>();
        path = new ArrayList<>();
        backtracking(nums, 0);
        return res;
    }

    private void backtracking(int[] nums, int start) {
        res.add(new ArrayList<Integer>(path));

        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtracking(nums, i + 1);
            path.remove(path.size() - 1);
        }
    }
}