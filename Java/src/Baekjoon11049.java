import java.io.*;
import java.util.*;

public class Baekjoon11049 {

    static StringTokenizer st;
    static int n;
    static int[][] ls;
    static int[][] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        ls = new int[n][2];
        dp = new int[n][n];

        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            ls[i][0] = Integer.parseInt(st.nextToken());
            ls[i][1] = Integer.parseInt(st.nextToken());
        }

        for(int i=0; i<n-1; i++) {
            dp[i][i+1] = ls[i][0]*ls[i][1]*ls[i+1][1];
        }

        for(int gap=2; gap<n; gap++) {
            for(int start=0; start+gap<n; start++) {
                int end = start+gap;
                dp[start][end] = Integer.MAX_VALUE;

                for(int mid=start; mid<end; mid++) {
                    dp[start][end] = Math.min(dp[start][end], dp[start][mid] + dp[mid+1][end] + ls[start][0]*ls[mid][1]*ls[end][1]);
                }
            }
        }
        System.out.println(dp[0][n-1]);
    }
}
