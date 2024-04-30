import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Baekjoon10799 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String pipe = br.readLine();
        int answer = 0;
        int tmp = 0;
        int left = 0;
        boolean check = false;

        for(int i=0; i<pipe.length(); i++) {
            if (pipe.charAt(i) == '(') {
                check = true;
                left++;
            } else {
                left--;
                if (check) {
                    check = false;
                    tmp += left;
                } else {
                    answer += tmp + 1;
                    tmp = 0;
                }
            }
        }
        br.close();
        System.out.println(answer);
    }
}
