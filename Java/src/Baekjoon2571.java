import java.io.*;
import java.util.*;

public class Baekjoon2571 {

    static int N;
    static int[][] board = new int[101][101];

    static int x;
    static int y;
    static int height;
    static int width;
    static int answer;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());

            for (int j=x; j<x+10; j++) {
                for (int k=y; k<y+10; k++) {
                    board[j][k] = 1;
                }
            }
        }

        for (int j=0; j<101; j++) {
            for (int i=0; i<100; i++) {
                if (board[i][j] != 0 && board[i+1][j] != 0) {
                    board[i+1][j] = board[i][j] + 1;
                }
            }
        }

        for (int i=0; i<101; i++) {
            for (int j=0; j<101; j++) {
                if (board[i][j] == 0) continue;
                height = board[i][j];
                width = 1;
                for (int k=j+1; k<101; k++) {
                    if (board[i][k] == 0) break;
                    if (board[i][k] < height) {
                        if (height * width > answer) answer = height * width;
                        height = board[i][k];
                    }
                    width++;
                }
                if (height * width > answer) answer = height * width;

            }
        }

        System.out.println(answer);
    }
}
