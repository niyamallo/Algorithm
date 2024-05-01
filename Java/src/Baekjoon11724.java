import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;


public class Baekjoon11724 {
    static ArrayList<Integer>[] A;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        A = new ArrayList[n+1];
        visited = new boolean[n+1];
        for(int i=1; i<n+1; i++) {
            A[i] = new ArrayList<Integer>();
        }
        for(int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            A[node1].add(node2);
            A[node2].add(node1);
        }
        int count = 0;
        for(int i=1; i<n+1; i++) {
            if(!visited[i]) {
                count++;
                DFS(i);
            }
        }
        System.out.println(count);
    }

    private static void DFS(int v) {
        if(visited[v]) {
            return;
        }
        visited[v] = true;
        for(int i: A[v]) {
            if(!visited[i]) {
                DFS(i);
            }
        }
    }
}
