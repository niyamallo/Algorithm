import java.io.*;
import java.util.*;

public class Baekjoon5073 {

    static int a, b, c;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            checkTriangle(a, b, c);
        }
    }

    static void checkTriangle(int a, int b, int c) {

        if (a == 0) {
            System.exit(0);
        }

        if (a+b<=c || a+c <=b || b+c <= a) {
            System.out.println("Invalid");
            return;
        }

        if (a == b && b == c) {
            System.out.println("Equilateral");
            return;
        }

        if (a == b || b == c || a == c) {
            System.out.println("Isosceles");
            return;
        }

        System.out.println("Scalene");
    }
}
