import java.io.*;
import java.util.*;

public class Baekjoon17404 {

    static int N;
    static int[][] houses;
    static int[] dp;
    static int r, g, b;
    static int answer;

    static final int INF = 1_000 * 1_000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        houses = new int[N][3];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            houses[i][0] = Integer.parseInt(st.nextToken());
            houses[i][1] = Integer.parseInt(st.nextToken());
            houses[i][2] = Integer.parseInt(st.nextToken());
        }

        answer = INF;

        for (int i=0; i<3; i++) {

            dp = new int[] {INF, INF, INF};
            dp[i] = houses[0][i];

            for (int j=1; j<N; j++) {
                r = houses[j][0] + Math.min(dp[1], dp[2]);
                g = houses[j][1] + Math.min(dp[0], dp[2]);
                b = houses[j][2] + Math.min(dp[0], dp[1]);
                dp[0] = r;
                dp[1] = g;
                dp[2] = b;
            }

            for (int j=0; j<3; j++) {
                if (i != j) {
                    answer = Math.min(answer, dp[j]);
                }
            }
        }
        System.out.println(answer);
    }
}
