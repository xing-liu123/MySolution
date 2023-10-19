class Solution {

    public String findDifferentBinaryString(String[] nums) {
        Set<String> set = new HashSet<>(Arrays.asList(nums));
        StringBuilder sb = new StringBuilder();
        if (backtracking(set, sb, nums.length)) {
            return sb.toString();
        }
        
        return "";
    }

    private boolean backtracking(Set<String> set, StringBuilder sb, int n) {
        if (sb.length() == n) {
            return !set.contains(sb.toString());
        }

        sb.append('0');
        if (backtracking(set, sb, n)) {
            return true;
        }
        sb.deleteCharAt(sb.length() - 1);

        sb.append('1');
        if (backtracking(set, sb, n)) {
            return true;
        }
        sb.deleteCharAt(sb.length() - 1);

        return false;
    }

}