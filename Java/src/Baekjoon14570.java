import java.util.*;
import java.io.*;

public class Baekjoon14570 {

    static int N;
    static int[][] tree;
    static long K;
    static int answer;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        tree = new int[N+1][2];
        for (int i=1; i<=N; i++) {
            st = new StringTokenizer(br.readLine());
            tree[i][0] = Integer.parseInt(st.nextToken());
            tree[i][1] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        K = Long.parseLong(st.nextToken());
        answer = dfs(1, K);
        System.out.println(answer);
    }

    static int dfs(int curNode, long target) {
        int leftChild = tree[curNode][0];
        int rightChild = tree[curNode][1];

        if (leftChild == -1 && rightChild == -1) {
            return curNode;
        } else if (leftChild != -1 && rightChild == -1) {
            return dfs(leftChild, target);
        } else if (leftChild == -1 && rightChild != -1) {
            return dfs(rightChild, target);
        } else {
            if (target % 2 == 0) {
                return dfs(rightChild, target/2);
            } else {
                return dfs(leftChild, target/2 + 1);
            }
        }
    }
}
