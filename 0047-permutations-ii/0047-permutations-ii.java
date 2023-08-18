class Solution {
    List<List<Integer>> res;
    List<Integer> path;
    int[] used;
    public List<List<Integer>> permuteUnique(int[] nums) {
        res = new ArrayList<>();
        path = new ArrayList<>();
        used = new int[nums.length];
        Arrays.sort(nums);
        helper(nums);
        return res;
    }

    private void helper(int[] nums) {
        if (path.size() == nums.length) {
            res.add(new ArrayList<Integer>(path));
        }

        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[ i - 1] && used[i - 1] == 1) {
                continue;
            }
            if (used[i] == 0) {
                path.add(nums[i]);
                used[i] = 1;
                helper(nums);
                path.remove(path.size() - 1);
                used[i] = 0;
            }
            
        }
    }
}