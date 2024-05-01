import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon11047 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] A = new int[N];
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            A[N-i-1] = Integer.parseInt(st.nextToken());
        }
        int count = 0;
        int idx = 0;
        while(M != 0) {
            count += M / A[idx];
            M = M % A[idx];
            idx++;
        }
        System.out.println(count);
    }
}
