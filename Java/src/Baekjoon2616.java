import java.io.*;
import java.util.*;

public class Baekjoon2616 {

    static int N;
    static int[] data;
    static int K;
    static int[][] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        data = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i=1; i<N+1; i++) {
            int eachData = Integer.parseInt(st.nextToken());
            data[i] = eachData;
        }
        for (int i=1; i<N+1; i++) {
            data[i] += data[i-1];
        }
        K = Integer.parseInt(br.readLine());
        dp = new int[4][N+1];

        for (int i=1; i<4; i++) {
            for (int j=i*K; j<N+1; j++) {
                dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-K] + data[j] - data[j-K]);
            }
        }

        System.out.println(dp[3][N]);
    }
}
