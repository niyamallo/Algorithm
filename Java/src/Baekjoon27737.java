import java.io.*;
import java.util.*;

public class Baekjoon27737 {

    static int N, M, K;
    static int[][] farm;
    static boolean[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};
    static boolean possible;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        possible = false;
        farm = new int[N][N];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                farm[i][j] = Integer.parseInt(st.nextToken());
                if (farm[i][j] == 0) possible = true;
            }
        }
        if (!possible) {
            System.out.println("IMPOSSIBLE");
            System.exit(0);
        }

        visited = new boolean[N][N];

        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (!visited[i][j] && farm[i][j] == 0) {
                    M = M - bfs(i, j);
                    if (M < 0) {
                        System.out.println("IMPOSSIBLE");
                        System.exit(0);
                    }
                }
            }
        }
        System.out.println("POSSIBLE");
        System.out.println(M);
    }

    static int bfs(int a, int b) {

        Queue<int[]> q = new LinkedList<>();
        int needs = 0;
        q.add(new int[]{a, b});
        visited[a][b] = true;

        while (!q.isEmpty()) {
            int[] now = q.poll();
            int x = now[0];
            int y = now[1];
            needs++;
            for (int i=0; i<4; i++) {
                int ii = x + dx[i];
                int jj = y + dy[i];
                if (ii<0 || ii>=N || jj<0 || jj>=N) continue;
                if (!visited[ii][jj] && farm[ii][jj] == 0) {
                    q.add(new int[]{ii,jj});
                    visited[ii][jj] = true;
                }
            }
        }
        if (needs%K == 0) {
            needs = needs/K;
        } else {
            needs = needs/K + 1;
        }
        return needs;
    }
}
