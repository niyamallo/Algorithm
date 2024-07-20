import java.io.*;
import java.util.*;

public class Baekjoon2559 {

    static int N;
    static int K;
    static int[] temperature;
    static int answer;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        temperature = new int[N+1];

        st = new StringTokenizer(br.readLine());
        temperature[0] = 0;
        for (int i=1; i<N+1; i++) {
            temperature[i] = temperature[i-1] + Integer.parseInt(st.nextToken());
        }

        answer = -10_000_000;
        for (int i=0; i<N-K+1; i++) {
            if (temperature[i+K] - temperature[i] > answer) {
                answer = temperature[i+K] - temperature[i];
            }
        }

        System.out.println(answer);

    }
}
