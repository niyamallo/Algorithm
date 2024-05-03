import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Stack;
import java.util.ArrayList;

public class Baekjoon1707 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int V;
    static int E;
    static int[] kind;
    static boolean[] visited;
    static ArrayList<Integer>[] node;
    static boolean flag;
    static Stack<Integer> stack;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        for(int tc=0; tc<K; tc++) {
            st = new StringTokenizer(br.readLine());
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());
            node = new ArrayList[V+1];
            kind = new int[V+1];
            visited = new boolean[V+1];
            flag = false;
            for(int i=1; i<V+1; i++) {
                node[i] = new ArrayList<Integer>();
            }
            for(int i=0; i<E; i++) {
                st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                node[start].add(end);
                node[end].add(start);
            }
            for(int i=1; i<V+1; i++) {
                if(!flag && !visited[i]) {
                    DFS(i);
                }
                if(flag) break;
            }
            if(flag) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
        }
    }

    private static void DFS(int v) {
        stack = new Stack<>();
        stack.add(v);
        kind[v] = 0;
        visited[v] = true;
        while(!stack.isEmpty()){
            int now = stack.pop();
            for(int i: node[now]) {
                if(visited[i]&&(kind[now]==kind[i])) {
                    flag = true;
                    return;
                }
                if(!visited[i]) {
                    visited[i] = true;
                    kind[i] = (kind[now] + 1) % 2;
                    stack.add(i);
                }
            }
        }
    }
}
