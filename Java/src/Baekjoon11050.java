import java.util.Scanner;

public class Baekjoon11050 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[][] table = new int[N+1][N+1];
        for(int i=0; i<N+1; i++) {
            for(int j=0; j<N+1; j++) {
                if(i==j) table[i][j] = 1;
                else if(j==0) table[i][j] = 1;
                else if(i<j) table[i][j] = 0;
            }
        }
        for(int i=1; i<N+1; i++) {
            for(int j=1; j<i+1; j++) {
                table[i][j] = table[i-1][j] + table[i-1][j-1];
            }
        }
        System.out.println(table[N][M]);
    }
}
