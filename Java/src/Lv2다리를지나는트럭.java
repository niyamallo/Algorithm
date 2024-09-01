import java.util.*;

class Lv2다리를지나는트럭 {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int curWeight = 0;
        Queue<Integer> queue = new LinkedList<>();

        for (int w: truck_weights) {
            while (true) {
                if (queue.isEmpty()) {
                    queue.offer(w);
                    curWeight += w;
                    answer++;
                    break;
                }
                if (queue.size() == bridge_length) {
                    curWeight -= queue.poll();
                }
                if (curWeight + w <= weight) {
                    queue.offer(w);
                    curWeight += w;
                    answer++;
                    break;
                }
                queue.offer(0);
                answer++;
            }
        }
        answer += bridge_length;

        return answer;
    }
}