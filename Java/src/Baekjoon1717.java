import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Baekjoon1717 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static int[] parent;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        parent = new int[N+1];
        for(int i=0; i<N+1; i++) {
            parent[i] = i;
        }
        int M = Integer.parseInt(st.nextToken());
        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int check = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if(check == 0) {
                union(a, b);
            } else {
                boolean result = checkSame(a, b);
                if(result) {
                    bw.write("YES"+"\n");
                } else {
                    bw.write("NO"+"\n");
                }
            }
        }
        bw.flush();
        br.close();
        bw.close();
    }

    private static void union(int a, int b) {
        a = find(a);
        b = find(b);
        if(a != b) {
            int small = Math.min(a,b);
            int big = Math.max(a,b);
            parent[big] = small;
        }
    }

    private static int find(int a) {
        if(a == parent[a]) return a;
        else {
            return parent[a] = find(parent[a]);
        }
    }

    private static boolean checkSame(int a, int b) {
        a = find(a);
        b = find(b);
        return a == b;
    }
}
