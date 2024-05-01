import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon1145 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] A = new int[5];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<5; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        int num = 1;
        int count = 0;
        while(true) {
            for (int i: A) {
                if(num%i == 0) count++;
            }
            if (count>=3) {
                System.out.println(num);
                return;
            }
            num++;
            count = 0;
        }
    }
}
