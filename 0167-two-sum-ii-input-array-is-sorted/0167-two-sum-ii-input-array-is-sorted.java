class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] res = new int[2];
       HashMap<Integer, Integer> map = new HashMap<>();

       for (int i = 0; i < numbers.length; i++) {
           if (map.containsKey(target - numbers[i])) {
               res[0] = map.get(target - numbers[i]);
               res[1] = i + 1;
           }
           map.put(numbers[i], i + 1);
       }

       return res;
    }
}