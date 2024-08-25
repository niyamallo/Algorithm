// bfs와 dfs를 재귀를 사용하지 않고 풀 수 있다는걸 설명하기 위해 구현한 방식
import java.io.*;
import java.util.*;

public class Baekjoon1260 {

    static BufferedReader br;
    static BufferedWriter bw;
    static int N, M, V;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {

        br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());
        graph = new ArrayList[N+1];
        for (int i=0; i<N+1; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            graph[v1].add(v2);
            graph[v2].add(v1);
        }
        for (int i=0; i<N+1; i++) {
            Collections.sort(graph[i], Collections.reverseOrder());
        }

        visited = new boolean[N+1];
        dfs(V);
        Arrays.fill(visited, false);
        System.out.println();

        for (int i=0; i<N+1; i++) {
            Collections.sort(graph[i]);
        }
        bfs(V);
        br.close();
        bw.close();
    }

    static void dfs(int v) throws IOException {
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Integer> st = new Stack<>();
        st.push(v);

        while (!st.isEmpty()) {
            int now = st.pop();
            if (!visited[now]) {
                bw.write(now + " ");
                visited[now] = true;
                for (int next : graph[now]) {
                    if (!visited[next]) {
                        st.push(next);
                    }
                }
            }
        }
        bw.flush();
    }

    static void bfs(int v) throws IOException {
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Queue<Integer> q = new LinkedList<>();
        q.offer(v);

        while (!q.isEmpty()) {
            int now = q.poll();
            if (!visited[now]) {
                bw.write(now + " ");
                visited[now] = true;
                for (int next : graph[now]) {
                    if (!visited[next]) q.offer(next);
                }
            }
        }
        bw.flush();
    }
}
