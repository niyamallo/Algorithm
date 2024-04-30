import java.util.Scanner;
import java.util.Stack;

public class Baekjoon1874 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        for(int i=0; i<N; i++) {
            A[i] = sc.nextInt();
        }
        Stack<Integer> stack = new Stack<>();
        int num = 1;
        boolean checked = true;
        StringBuffer bf = new StringBuffer();
        for(int i=0; i<N; i++) {
            if (A[i] >= num) {
                while (A[i] >= num) {
                    stack.push(num++);
                    bf.append("+\n");
                }
                stack.pop();
                bf.append("-\n");
            } else {
                if (stack.pop() > A[i]) {
                    System.out.println("NO");
                    checked = false;
                    break;
                } else {
                    bf.append("-\n");
                }
            }
        }
        if (checked) {
            System.out.println(bf.toString());
        }
    }
}
