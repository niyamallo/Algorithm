import java.util.Scanner;

public class Baekjoon2018 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int count = 1;
        int start_index = 1;
        int end_index = 1;
        int sum = 1;
        while(end_index < N) {
            if(sum == N) {
                count++; sum += ++end_index;
            } else if (sum > N) {
                sum -= start_index++;
            } else {
                sum += ++end_index;
            }
        }
        System.out.println(count);
    }
}
