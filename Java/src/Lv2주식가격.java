import java.util.*;

class Lv2주식가격 {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Stack<Integer> st = new Stack<>();

        for (int i=0; i<prices.length; i++) {
            while (!st.isEmpty() && prices[i] < prices[st.peek()]) {
                answer[st.peek()] = i - st.peek();
                st.pop();
            }
            st.push(i);
        }

        while (!st.isEmpty()) {
            answer[st.peek()] = prices.length - st.pop() - 1;
        }

        return answer;
    }
}