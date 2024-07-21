import java.io.*;
import java.util.*;

public class Baekjoon25305 {

    static int N;
    static int k;
    static Integer[] scores;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        scores = new Integer[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            scores[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(scores, Collections.reverseOrder());

        System.out.println(scores[k-1]);
    }
}
