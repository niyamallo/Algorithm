import java.io.*;
import java.util.*;

public class Baekjoon1922 {

    static class Edge implements Comparable<Edge> {

        int v1, v2, cost;

        public Edge(int v1, int v2, int cost) {
            this.v1 = v1;
            this.v2 = v2;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge e) {
            return cost - e.cost;
        }
    }

    static int N, M;
    static int[] parents;
    static Edge edge;
    static PriorityQueue<Edge> queue;
    static int v1, v2, cost;
    static int answer;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        parents = new int[N+1];
        for (int i=1; i<N+1; i++) {
            parents[i] = i;
        }
        queue = new PriorityQueue<>();
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            v1 = Integer.parseInt(st.nextToken());
            v2 = Integer.parseInt(st.nextToken());
            cost = Integer.parseInt(st.nextToken());
            Edge edge = new Edge(v1, v2, cost);
            queue.add(edge);
        }

        answer = 0;
        while(!queue.isEmpty()) {
            Edge cur = queue.poll();
            if (findParents(cur.v1) != findParents(cur.v2)) {
                union((cur.v1), (cur.v2));
                answer += cur.cost;
            }
        }

        System.out.println(answer);
    }

    static int findParents(int v) {
        if (parents[v] != v) {
            return parents[v] = findParents(parents[v]);
        }
        return v;
    }

    static void union(int v1, int v2) {
        int p1 = findParents(v1);
        int p2 = findParents(v2);

        if (p1 != p2) {
            parents[p1] = p2;
        }
    }
}