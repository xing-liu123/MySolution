class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        int[] res = new int[3];
        for (int i = 0; i < triplets.length; i++) {
            int[] triplet = triplets[i];

            if (triplet[0] > target[0] || triplet[1] > target[1] || triplet[2] > target[2]) {
                continue;
            }

            if (triplet[0] == target[0]) {
                res[0] = Math.max(res[0], triplet[0]);
                res[1] = Math.max(res[1], triplet[1]);
                res[2] = Math.max(res[2], triplet[2]);
            }

            if (triplet[1] == target[1]) {
                res[0] = Math.max(res[0], triplet[0]);
                res[1] = Math.max(res[1], triplet[1]);
                res[2] = Math.max(res[2], triplet[2]);
            }

            if (triplet[2] == target[2]) {
                res[0] = Math.max(res[0], triplet[0]);
                res[1] = Math.max(res[1], triplet[1]);
                res[2] = Math.max(res[2], triplet[2]);
            }

            if (res[0] == target[0] && res[1] == target[1] && res[2] == target[2]) {
                return true;
            }
        }

        return false;

        


    }
}