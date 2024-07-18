import java.io.*;

public class Baekjoon1509 {

    static String str;
    static int N;
    static boolean[][] checkP;
    static int[] dp;


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = br.readLine();
        N = str.length();
        checkP = new boolean[N][N];
        dp = new int[N+1];
        for (int i=1; i<N+1; i++) {
            dp[i] = 2500;
        }

        for (int i=0; i<N; i++) {
            checkP[i][i] = true;
        }

        for (int i=1; i<N; i++) {
            if (str.charAt(i-1) == str.charAt(i)) {
                checkP[i - 1][i] = true;
            }
        }

        for (int len=3; len<N+1; len++) {
            for (int start=0; start<N-len+1; start++) {
                int end = start + len - 1;
                if (str.charAt(start) == str.charAt(end) && checkP[start+1][end-1]) {
                    checkP[start][end] = true;
                }
            }
        }

        for (int end=1; end<N+1; end++) {
            for (int start=1; start<end+1; start++) {
                if (checkP[start-1][end-1]) {
                    dp[end] = Math.min(dp[end], dp[start-1] + 1);
                } else {
                    dp[end] = Math.min(dp[end], dp[end-1] + 1);
                }
            }
        }

        System.out.println(dp[N]);
    }
}
