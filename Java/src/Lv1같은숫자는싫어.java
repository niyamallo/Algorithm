import java.util.*;

public class Lv1같은숫자는싫어 {
    public int[] solution(int []arr) {
        int[] answer;
        Stack<Integer> st = new Stack<>();

        st.push(arr[0]);
        for (int i=1; i<arr.length; i++) {
            if (st.peek() != arr[i]) st.push(arr[i]);
        }

        answer = new int[st.size()];
        for (int i=st.size()-1; i>=0; i--) {
            answer[i] = st.pop();
        }

        return answer;
    }
}
