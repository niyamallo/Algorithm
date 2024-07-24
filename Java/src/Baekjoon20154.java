import java.io.*;

public class Baekjoon20154 {

    static int[] alp = new int[] {3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1};
    static int answer;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        for (int i=0; i<str.length(); i++) {
            answer += alp[(str.charAt(i) - 65)];
            answer %= 10;
        }

        if (answer % 2 == 1) {
            System.out.println("I'm a winner!");
        } else {
            System.out.println("You're the winner?");
        }
    }
}
