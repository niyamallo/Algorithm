import java.util.*;

class Lv2프로세스 {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int priority: priorities) {
            pq.offer(priority);
        }

        while (!pq.isEmpty()) {
            for (int i=0; i<priorities.length; i++) {
                if (pq.peek() == priorities[i]) {
                    pq.poll();
                    answer++;

                    if (location == i) return answer;
                }
            }
        }

        return answer;
    }
}