import java.util.*;

public class Baekjoon1562 {

    static int N;
    static final int MOD = 1_000_000_000;
    static long[][][] dp;
    static long answer;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        dp = new long[N+1][10][1<<10];

        for (int j=1; j<10; j++) {
            dp[1][j][1<<j] = 1;
        }

        for (int i=2; i<N+1; i++) {
            for (int j=0; j<10; j++) {
                for (int k=0; k<1024; k++) {
                    int bit = k | (1<<j);
                    if (0 < j) dp[i][j][bit] += dp[i-1][j-1][k];
                    if (j < 9) dp[i][j][bit] += dp[i-1][j+1][k];
                    dp[i][j][bit] %= MOD;
                }
            }
        }

        answer = 0;
        for (int j=0; j<10; j++) {
            answer += dp[N][j][1023];
            answer %= MOD;
        }

        System.out.println(answer);
    }
}
