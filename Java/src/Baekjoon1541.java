import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Baekjoon1541 {
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split("-");
        for(int i=0; i<str.length; i++) {
            if(i==0) {
                answer += mySum(str[i]);
            } else {
                answer -= mySum(str[i]);
            }
        }
        System.out.println(answer);
    }

    private static int mySum(String s) {
        int sum = 0;
        String[] tmp = s.split("\\+");
        for(int i=0; i<tmp.length; i++) {
            sum += Integer.parseInt(tmp[i]);
        }
        return sum;
    }
}
