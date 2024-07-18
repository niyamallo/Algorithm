import java.io.*;
import java.util.*;

public class Baekjoon2467 {

    static int N;
    static int[] solutions;
    static int start, end;
    static int total = 2_000_000_000;
    static int A, B;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        solutions = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            solutions[i] = Integer.parseInt(st.nextToken());
        }

        start = 0;
        end = N-1;
        while (start < end) {
            int tmp = solutions[start] + solutions[end];
            if (Math.abs(tmp) <= total) {
                total = Math.abs(tmp);
                A = solutions[start];
                B = solutions[end];
            }

            if (0 < tmp) {
                end--;
            } else {
                start++;
            }
        }

        System.out.println(A + " " + B);
    }
}
