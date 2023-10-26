class Solution {
    public int[] getOrder(int[][] tasks) {
        int[][] sortedTasks = new int[tasks.length][3];

        for (int i = 0; i < tasks.length; i++) {
            sortedTasks[i][0] = tasks[i][0];
            sortedTasks[i][1] = tasks[i][1];
            sortedTasks[i][2] = i;
        }

        Arrays.sort(sortedTasks, (a, b) -> Integer.compare(a[0], b[0]));

        PriorityQueue<int[]> nextTask = new PriorityQueue<>((a, b) -> (a[1] != b[1] ? (a[1] - b[1]) : (a[2] - b[2])));

        int[] order = new int[tasks.length];

        int time = 0;
        int taskIndex = 0;
        int ansIndex = 0;

        while (taskIndex < tasks.length || !nextTask.isEmpty()) {
            if (nextTask.isEmpty() && time < sortedTasks[taskIndex][0]) {
                time = sortedTasks[taskIndex][0];
            }

            while (taskIndex < tasks.length && time >= sortedTasks[taskIndex][0]) {
                nextTask.add(sortedTasks[taskIndex++]);
            }

            int processTime = nextTask.peek()[1];
            int index = nextTask.peek()[2];
            nextTask.remove();

            time += processTime;
            order[ansIndex++] = index;
        } 

        return order;

    }
}