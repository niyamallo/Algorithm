import java.io.*;
import java.util.*;

public class Baekjoon14925 {

    static int N;
    static int M;
    static int[][] farm;
    static int[][] dp;
    static int answer;


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        farm = new int[N][M];
        dp = new int[N+1][M+1];
        answer = 0;
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<M; j++) {
                farm[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i=1; i<N+1; i++) {
            for (int j=1; j<M+1; j++) {
                if (farm[i-1][j-1] == 0) {
                    dp[i][j] = Math.min(Math.min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
                    if (dp[i][j] > answer) answer = dp[i][j];
                }
            }
        }

        System.out.println(answer);

    }
}
