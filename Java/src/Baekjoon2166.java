import java.io.*;
import java.util.*;

public class Baekjoon2166 {

    static int N;
    static long[][] vertex;
    static long doubleArea;
    static String area;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        vertex = new long[N+1][2];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            vertex[i][0] = Integer.parseInt(st.nextToken());
            vertex[i][1] = Integer.parseInt(st.nextToken());
        }
        vertex[N][0] = vertex[0][0];
        vertex[N][1] = vertex[0][1];

        doubleArea = 0;
        for (int i=0; i<N; i++) {
            doubleArea += vertex[i][1] * vertex[i+1][0] - vertex[i+1][1] * vertex[i][0];
        }

        area = String.format("%.1f", Math.abs(doubleArea/2.0));

        System.out.println(area);

    }
}
