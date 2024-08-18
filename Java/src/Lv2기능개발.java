import java.util.*;

class Lv2기능개발 {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer;
        ArrayList<Integer> tmp = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();

        for (int i=0; i<progresses.length; i++) {
            queue.add((int)Math.ceil((100.0 - progresses[i]) / speeds[i]));
        }

        int cnt = 0;
        int complete = queue.peek();
        while (!queue.isEmpty()) {
            if (queue.peek() <= complete) {
                queue.poll();
                cnt++;
            } else {
                tmp.add(cnt);
                cnt = 0;
                complete = queue.peek();
            }
        }
        if (cnt != 0) tmp.add(cnt);

        answer = new int[tmp.size()];
        for (int i=0; i<tmp.size(); i++) {
            answer[i] = tmp.get(i);
        }
        return answer;
    }
}
