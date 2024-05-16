import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon2449 {

    final static int INF = 1<<30;
    static int[] idx;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        idx = new int[N+1];
        dp = new int[N+1][N+1];

        st = new StringTokenizer(br.readLine());
        for(int i=1; i<=N; i++) {
            idx[i] = Integer.parseInt(st.nextToken());
            if(idx[i] == idx[i-1]) {
                N--;
                i--;
            }
        }

        for(int i=1; i<=N; i++) {
            for(int j=1; j<=N; j++) {
                dp[i][j] = INF;
            }
            dp[i][i] = 0;
        }

        for(int size=2; size<=N; size++) {
            for(int start=1; start<=N-size+1; start++) {
                int end = start + size - 1;
                for(int mid=start; mid<end; mid++) {
                    int newValue = dp[start][mid] + dp[mid+1][end];
                    if(idx[start] != idx[mid+1]) {
                        newValue++;
                    }
                    dp[start][end] = Math.min(dp[start][end], newValue);
                }
            }
        }

        System.out.println(dp[1][N]);
        br.close();
    }
}
