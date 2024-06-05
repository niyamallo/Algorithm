import java.io.*;
import java.util.*;

class Edge implements Comparable<Edge> {
    int v1;
    int v2;
    int value;

    public Edge(int v1, int v2, int value) {
        this.v1 = v1;
        this.v2 = v2;
        this.value = value;
    }

    @Override
    public int compareTo(Edge e) {
        return value - e.value;
    }
}
public class Baekjoon1197 {

    static StringTokenizer st;
    static int v;
    static int e;
    static int v1;
    static int v2;
    static int value;
    static int[] parents;
    static PriorityQueue<Edge> queue;
    static int total;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        queue = new PriorityQueue<Edge>();
        parents = new int[v+1];

        for (int i=0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            v1 = Integer.parseInt(st.nextToken());
            v2 = Integer.parseInt(st.nextToken());
            value = Integer.parseInt(st.nextToken());
            queue.add(new Edge(v1, v2, value));
        }
        for (int i=0; i<v+1; i++) {
            parents[i] = i;
        }

        while (!queue.isEmpty()) {
            Edge cur = queue.poll();
            if (findParent(cur.v1) != findParent(cur.v2)) {
                union((cur.v1), (cur.v2));
                total += cur.value;
            }
        }

        System.out.println(total);
    }

    static int findParent(int x) {
        if (parents[x] != x) {
            return parents[x] = findParent(parents[x]);
        }
        return x;
    }

    static void union(int x, int y) {
        int p1 = findParent(x);
        int p2 = findParent(y);

        if (p1 != p2) {
            parents[p1] = p2;
        }
    }
}
