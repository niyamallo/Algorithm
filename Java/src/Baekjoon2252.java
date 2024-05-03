import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;

public class Baekjoon2252 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static int[] degree;
    static ArrayList<ArrayList<Integer>> list;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        list = new ArrayList<>();
        degree = new int[N+1];
        for(int i=0; i<N+1; i++) {
            list.add(new ArrayList<>());
            degree[i] = 0;
        }
        int M = Integer.parseInt(st.nextToken());
        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list.get(a).add(b);
            degree[b]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for(int i=1; i<N+1; i++) {
            if(degree[i] == 0) {
                queue.add(i);
            }
        }
        while(!queue.isEmpty()) {
            int now = queue.poll();
            bw.write(now + " ");
            for(int next: list.get(now)){
                degree[next]--;
                if(degree[next] == 0) {
                    queue.add(next);
                }
            }
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
