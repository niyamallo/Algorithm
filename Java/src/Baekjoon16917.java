import java.util.Scanner;

public class Baekjoon16917 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] inputs = input.split(" ");
        int A = Integer.parseInt(inputs[0]);
        int B = Integer.parseInt(inputs[1]);
        int C = Integer.parseInt(inputs[2]);
        int X = Integer.parseInt(inputs[3]);
        int Y = Integer.parseInt(inputs[4]);
        int answer;

        answer = getTotal(A, B, C, X, Y);

        System.out.println(answer);
    }

    static int getTotal(int A, int B ,int C, int X, int Y) {
        int seperate;
        int mix;
        int mixOver;
        int answer;

        seperate = A * X + B * Y;
        if (X > Y) {
            mix = (2 * C * Y) + (A * (X - Y));
            mixOver = (2 * C * X);
        } else {
            mix = (2 * C * X) + (B * (Y - X));
            mixOver = (2 * C * Y);
        }

        answer = Math.min(seperate, mix);
        answer = Math.min(answer, mixOver);
        return answer;
    }
}
