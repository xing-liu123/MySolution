class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);

        int i = 0, j = people.length - 1;
        int count = 0;
        while(i < j) {
            if (people[i] + people[j] <= limit) {
                i++;
                
            } 

            j--;
            count++;
        }

        return i == j ? count + 1 : count;
    }
}