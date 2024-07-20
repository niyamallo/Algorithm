import java.io.*;
import java.util.*;

public class Baekjoon14215 {

    static int[] lines;
    static int tmp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        lines = new int[3];
        for (int i=0; i<3; i++) {
            lines[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(lines);

        tmp = lines[0] + lines[1] - 1;
        if (tmp < lines[2]) {
            lines[2] = tmp;
        }

        System.out.println(lines[0] + lines[1] + lines[2]);
    }
}
