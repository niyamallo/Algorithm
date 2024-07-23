import java.io.*;
import java.util.*;

public class Baekjoon1414 {

    static class Edge implements Comparable<Edge> {

        int i, j, length;

        public Edge(int i, int j, int length) {
            this.i = i;
            this.j = j;
            this.length = length;
        }

        @Override
        public int compareTo(Edge e) {
            return this.length - e.length;
        }
    }

    static int N;
    static int[] parent;
    static char[][] lengthData;
    static PriorityQueue<Edge> pq;
    static int total;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        parent = new int[N+1];
        for (int i=1; i<N+1; i++) {
            parent[i] = i;
        }
        lengthData = new char[N][N];
        for (int i=0; i<N; i++) {
            lengthData[i] = br.readLine().toCharArray();
        }

        pq = new PriorityQueue<>();
        total = 0;
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (lengthData[i][j] == '0') continue;
                if ('a' <= lengthData[i][j] && lengthData[i][j] <= 'z') {
                    total += lengthData[i][j] - 96;
                    pq.add(new Edge(i+1, j+1, lengthData[i][j] - 96));
                } else {
                    total += lengthData[i][j] - 38;
                    pq.add(new Edge(i+1, j+1, lengthData[i][j] - 38));
                }
            }
        }

        while (!pq.isEmpty()) {
            Edge now = pq.poll();
            int n1 = now.i;
            int n2 = now.j;
            int length = now.length;

            if (findParent(n1) != findParent(n2)) {
                union(n1, n2);
                total -= length;
            }
        }

        boolean flag = false;
        for (int i=1; i<N+1; i++) {
            if (findParent(i) != findParent(1)) {
                System.out.println("-1");
                flag = true;
                break;
            }
        }
        if (!flag) System.out.println(total);
    }

    static int findParent(int x) {
        if (parent[x] != x) {
            return parent[x] = findParent(parent[x]);
        }
        return x;
    }

    static void union(int n1, int n2) {

        n1 = findParent(n1);
        n2 = findParent(n2);

        if (n1 != n2) {
            parent[n1] = n2;
        }
    }
}
