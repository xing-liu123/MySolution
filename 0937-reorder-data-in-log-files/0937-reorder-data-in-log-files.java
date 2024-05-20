class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Arrays.sort(logs, (a, b) -> { 
            String[] split_a = a.split(" ", 2);
            String[] split_b = b.split(" ", 2);
            
            boolean a_is_digit = Character.isDigit(split_a[1].charAt(0));
            boolean b_is_digit = Character.isDigit(split_b[1].charAt(0));

            
            if (a_is_digit && b_is_digit){
                return 0;
            } else if (a_is_digit && !b_is_digit) {
                return 1;
            } else if (!a_is_digit && b_is_digit) {
                return -1;
            } else {
                int cmp = split_a[1].compareTo(split_b[1]);
                
                return cmp == 0 ? split_a[0].compareTo(split_b[0]) : cmp;
            }
            
            
        });
        
        return logs;    
    }
}