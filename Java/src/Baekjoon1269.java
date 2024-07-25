import java.io.*;
import java.util.*;

public class Baekjoon1269 {

    static int A, B;
    static boolean[] check;
    static int a, b;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        check = new boolean[100_000_001];

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<A; i++) {
            check[Integer.parseInt(st.nextToken())] = true;
        }

        a = A;
        b = B;
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<B; i++) {
            if (check[Integer.parseInt(st.nextToken())]) {
                a--;
                b--;
            }
        }

        System.out.println(a + b);
    }
}
