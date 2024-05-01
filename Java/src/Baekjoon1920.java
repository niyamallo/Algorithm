import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Baekjoon1920 {

    static int N;
    static int[] A;
    static int M;
    static int[] B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        A = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        B = new int[M];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<M; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }
        for(int i : B) {
            bw.write(Search(i)+"\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
    private static int Search(int n) {
        int start = 0;
        int end = N-1;
        int mid;
        while(start<=end) {
            mid = (start+end)/2;
            if(A[mid] < n) {
                start = mid+1;
            } else if (n < A[mid]) {
                end = mid-1;
            } else {
                return 1;
            }
        }
        return 0;
    }
}
