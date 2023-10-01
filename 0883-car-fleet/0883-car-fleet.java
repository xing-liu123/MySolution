class Solution {
    class Car {
        int position;
        double time;

        Car(int pos, double time) {
            this.position = pos;
            this.time = time;
        }
    }
    public int carFleet(int target, int[] position, int[] speed) {
        Car[] cars = new Car[position.length];

        for (int i = 0; i < position.length; i++) {
            double time = (double)(target - position[i])/speed[i];
            cars[i] = new Car(position[i], time);
        } 

        Arrays.sort(cars, (a, b)->Integer.compare(a.position, b.position));
        
        Stack<Double> stack = new Stack<>(); 
        int res = 0;

        for (Car car : cars) {
           while(!stack.isEmpty() && car.time >= stack.peek()) {
                stack.pop(); 
            }
            stack.push(car.time);
        }

        return stack.size();
    }
}