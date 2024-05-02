import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Baekjoon1929 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int M;
    static int N;
    static boolean[] nums;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        decimalCheck(M, N);
        br.close();
    }

    private static void decimalCheck(int m, int n) throws IOException {
        nums = new boolean[n+1];
        for(int i=2; i<=Math.sqrt(n); i++) {
            if(nums[i]) continue;
            for(int j=i+i; j<=n; j=j+i) {
                nums[j] = true;
            }
        }
        int small = Math.max(2, m);
        for(int i=small; i<=n; i++) {
            if(!nums[i]) {
                bw.write(i + "\n");
            }
        }
        bw.flush();
        bw.close();
    }
}
