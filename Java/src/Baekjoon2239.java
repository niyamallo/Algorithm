import java.io.*;
import java.util.*;

public class Baekjoon2239 {

    static int[][] sudoku = new int[9][9];
    static ArrayList<int[]> zero = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for(int i=0; i<9; i++) {
            String str = br.readLine();
            for (int j=0; j<9; j++) {
                sudoku[i][j] = str.charAt(j) - '0';
                if (sudoku[i][j] == 0) {
                    zero.add(new int[] {i, j});
                }
            }
        }
        dfs(0);
    }

    static boolean[] check(int x, int y) {
        boolean[] possible = new boolean[10];
        for(int i=0; i<9; i++) {
            possible[sudoku[i][y]] = true;
        }
        for(int j=0; j<9; j++) {
            possible[sudoku[x][j]] = true;
        }
        int weight = 3 * (x/3);
        int height = 3 * (y/3);
        for(int i=weight; i<weight+3; i++) {
            for(int j=height; j<height+3; j++) {
                possible[sudoku[i][j]] = true;
            }
        }

        return possible;
    }

    static void dfs(int depth) {

        if (zero.size() == depth) {
            for(int i=0; i<9; i++) {
                for (int j=0; j<9; j++) {
                    System.out.print(sudoku[i][j]);
                }
                System.out.println();
            }
            System.exit(0);
        }

        int x = zero.get(depth)[0];
        int y = zero.get(depth)[1];
        boolean[] possible = check(x, y);
        for(int i=1; i<10; i++) {
            if(!possible[i]) {
                sudoku[x][y] = i;
                dfs(depth + 1);
                sudoku[x][y] = 0;
            }
        }
    }
}
