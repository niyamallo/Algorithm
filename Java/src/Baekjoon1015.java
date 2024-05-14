import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Baekjoon1015 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static int N;
    static int[] A;
    static int[] tempA;
    static int[] B;
    static int[] check;
    static int[] sumCheck;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        tempA = new int[1001];
        B = new int[N];
        check = new int[N+1];
        sumCheck = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
            check[A[i]]++;
        }
        for(int i=1; i<N+1; i++) {
            sumCheck[i] = sumCheck[i-1] + check[i];
        }
        for(int i=0; i<N;i++) {
            bw.write(sumCheck[A[i]-1] + " ");
            sumCheck[A[i]-1]++;
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
