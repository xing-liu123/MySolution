class Solution {
    List<Long> nums = new ArrayList<>();

    public boolean splitString(String s) {
        return backtracking(s, 0);    
    }

    private boolean backtracking(String s, int idx) {
        if (idx == s.length()) {
            return nums.size() > 1;
        }

        long currNum = 0;
        
        for (int i = idx; i < s.length(); i++) {
            currNum = currNum * 10 + (s.charAt(i) - '0');

            if (!nums.isEmpty() && currNum > nums.get(nums.size() - 1) - 1) {
                break;
            }

            if (nums.isEmpty() || currNum == nums.get(nums.size() - 1) - 1) {
                nums.add(currNum);
                if (backtracking(s, i + 1)) {
                    return true;
                }
                nums.remove(nums.size() - 1);
            }
        }

        return false;
    }
}