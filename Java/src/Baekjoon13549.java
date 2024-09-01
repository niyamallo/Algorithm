import java.io.*;
import java.util.*;

public class Baekjoon13549 {

    static int N, K;
    static int[] visited;
    static Deque<Integer> q;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        visited = new int[100001];
        Arrays.fill(visited, -1);
        q = new LinkedList<>();
        q.offer(N);
        visited[N] = 0;

        while (!q.isEmpty()) {
            int cur = q.poll();
            if (cur == K) {
                System.out.println(visited[cur]);
                System.exit(0);
            }
            for (int next: new int[] {2*cur, cur-1, cur+1}) {
                if (next < 0 || next > 100000) continue;
                if (visited[next] != -1) continue;
                if (next == 2*cur) {
                    visited[next] = visited[cur];
                    q.offerFirst(next);
                    continue;
                }
                visited[next] = visited[cur] + 1;
                q.offer(next);
            }
        }
    }
}
