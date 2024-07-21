import java.io.*;
import java.util.*;

public class Baekjoon2638 {

    static int N;
    static int M;
    static Queue<int[]> cheese;
    static Queue<int[]> newCheese;
    static Queue<int[]> delCheese;
    static int[][] board;
    static int count;
    static int time;
    static int[] dx = new int[] {1, 0, -1, 0};
    static int[] dy = new int[] {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        cheese = new LinkedList<>();
        newCheese = new LinkedList<>();
        delCheese = new LinkedList<>();
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                if (Integer.parseInt(st.nextToken()) == 1) {
                    board[i][j] = 1;
                    cheese.add(new int[] {i, j});
                    count++;
                }
            }
        }

        while (count != 0) {
            while (!cheese.isEmpty()) {
                int[] now = cheese.poll();
                int now_x = now[0];
                int now_y = now[1];
                int tmp = 0;
                for (int i=0; i<4; i++) {
                    if (board[now_x + dx[i]][now_y + dy[i]] == 0) tmp++;
                }
                if (tmp >= 2) {
                    count--;
                    delCheese.add(now);
                } else {
                    newCheese.add(now);
                }
            }

            while (!delCheese.isEmpty()) {
                int[] now = delCheese.poll();
                board[now[0]][now[1]] = 0;
            }

            time++;
            cheese = new LinkedList<>(newCheese);
            newCheese.clear();
        }

        System.out.println(time);
    }
}
