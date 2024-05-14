import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.StringTokenizer;
import java.util.ArrayList;


public class Baekjoon1450 {

    static int N;
    static int C;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        ArrayList<Integer> weight1 = new ArrayList<>();
        ArrayList<Integer> weight2 = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i<N; i++) {
            if (i < N/2) {
                weight1.add(Integer.parseInt(st.nextToken()));
            }
            else {
                weight2.add(Integer.parseInt(st.nextToken()));
            }
        }

        ArrayList<Integer> sum1 = new ArrayList<>();
        ArrayList<Integer> sum2 = new ArrayList<>();

        dfs(0, 0, weight1, sum1);
        dfs(0, 0, weight2, sum2);

        Collections.sort(sum2);
        int answer = 0;
        for (int i = 0; i < sum1.size(); i++) {
            int searchValue = C - sum1.get(i);
            answer += binarySearch(sum2, searchValue) + 1;
        }
        bw.write(String.valueOf(answer));
        bw.flush();

        br.close();
        bw.close();
    }

    public static void dfs(int idx, int sum, ArrayList<Integer> weight, ArrayList<Integer> answer) {
        if (sum > C) return;
        if (idx == weight.size()) {
            answer.add(sum);
            return;
        }
        dfs(idx+1, sum + weight.get(idx), weight, answer);
        dfs(idx+1, sum, weight, answer);
    }

    public static int binarySearch(ArrayList<Integer> sum, int target) {
        int left = 0, right = sum.size() - 1, mid = -1, answer = -1;
        while ( left <= right) {
            mid = (left + right) / 2;
            if (sum.get(mid) <= target) {
                answer = mid;
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return answer;
    }
}
