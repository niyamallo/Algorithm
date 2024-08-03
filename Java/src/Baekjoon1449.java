import java.io.*;
import java.util.*;

public class Baekjoon1449 {

    static int N, L;
    static int[] holes;
    static int count;
    static int range;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        holes = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            holes[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(holes);

        count = 0;
        range = 0;

        for (int now: holes) {
            if (now > range) {
                range = now + L - 1;
                count++;
            }
        }

        System.out.println(count);

    }
}
