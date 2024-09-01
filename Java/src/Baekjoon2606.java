import java.io.*;
import java.util.*;

public class Baekjoon2606 {

    static int N, connect;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        connect = Integer.parseInt(br.readLine());
        graph = new ArrayList[N+1];
        for (int i=0; i<N+1; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i=0; i<connect; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            graph[v1].add(v2);
            graph[v2].add(v1);
        }
        visited = new boolean[N+1];

        System.out.println(dfs(1));

    }

    static int dfs(int v) {
        Stack<Integer> st = new Stack<>();
        int answer = -1; //1번 컴퓨터는 counting이 안 됨.
        st.push(v);

        while (!st.isEmpty()) {
            int now = st.pop();
            if (!visited[now]) {
                visited[now] = true;
                answer++;
                for (int next : graph[now]) {
                    if (!visited[next]) st.push(next);
                }
            }
        }

        return answer;

    }
}
