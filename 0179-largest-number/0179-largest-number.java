class Solution {
    public String largestNumber(int[] nums) {
        String[] strs = new String[nums.length];

        for (int i = 0; i < nums.length; i++) {
            strs[i] = nums[i] + "";
        }

        Arrays.sort(strs, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                return (s1 + s2).compareTo(s2 + s1);
            }
        });

        if (strs[strs.length - 1].equals("0")) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        for (int i = strs.length - 1; i >= 0; i--) {
            
            sb.append(strs[i]);
            
        }

        return sb.toString();
    }
}