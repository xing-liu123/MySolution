class Solution {
    List<List<Integer>> res;
    List<Integer> path;
    int[] used;
    public List<List<Integer>> permute(int[] nums) {
        res = new ArrayList<>();
        path = new ArrayList<>();
        used = new int[nums.length];
        backtracking(nums);
        return res;
    }

    private void backtracking(int[] nums) {
      if(path.size() == nums.length) {
          res.add(new ArrayList<Integer>(path));
          return;
      }

      for (int i = 0; i < nums.length; i++) {
          if (used[i] == 0) {
              path.add(nums[i]);
              used[i] = 1;
              backtracking(nums);
              used[i] = 0;
              path.remove(path.size() - 1);
          } 
      }
    }
}