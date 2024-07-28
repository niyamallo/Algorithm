import java.io.*;
import java.util.*;

public class Baekjoon11279 {

    static int N;
    static PriorityQueue<Integer> pq;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i=0; i<N; i++) {
            int command = Integer.parseInt(br.readLine());
            if (command == 0 && pq.isEmpty()) {
                System.out.println(0);
                continue;
            }
            if (command == 0) {
                System.out.println(pq.poll());
                continue;
            }
            pq.add(command);
        }
    }
}
