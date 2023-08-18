class Solution {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> path = new ArrayList<>();;
    public List<List<Integer>> subsetsWithDup(int[] nums) {
       Arrays.sort(nums);
       backtracking(nums, 0);
       return res;
    }

    private void backtracking(int[] nums, int start) {
       res.add(new ArrayList<Integer>(path));

       for (int i = start; i < nums.length; i++) {
           if (i > start && nums[i] == nums[i - 1]) {
               continue;
           }
           path.add(nums[i]);
           backtracking(nums, i + 1);
            path.remove(path.size() - 1);
       }
    }
}