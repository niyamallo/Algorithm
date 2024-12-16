import java.io.*;
import java.util.*;

public class Baekjoon7576 {

    static int M, N;
    static int[][] box;
    static boolean[][] visited;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int time;

    public static void main(String[] args) throws IOException {

        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        box = new int[N][M];
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<M; j++) {
                box[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        visited = new boolean[N][M];

        // bfs
        bfs();

        // 출력
        time = 0;
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (box[i][j] == 0) {
                    System.out.println(-1);
                    System.exit(0);
                }
                time = Math.max(time, box[i][j]);
            }
        }
        System.out.println(time - 1);

    }

    static void bfs() {

        Queue<int[]> q = new LinkedList<>();
        int[] now;
        int nowX, nowY;

        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (box[i][j] == 1) {
                    q.offer(new int[] {i, j});
                    visited[i][j] = true;
                }
            }
        }

        while (!q.isEmpty()) {
            now = q.poll();
            nowX = now[0];
            nowY = now[1];
            for (int i=0; i<4; i++) {
                int nx = nowX + dx[i];
                int ny = nowY + dy[i];
                if (nx<0 || nx>=N || ny<0 || ny>=M) continue;
                if (box[nx][ny] == -1) continue;
                if (visited[nx][ny]) continue;
                visited[nx][ny] = true;
                q.offer(new int[] {nx, ny});
                box[nx][ny] = box[nowX][nowY] + 1;
            }
        }
    }
}
