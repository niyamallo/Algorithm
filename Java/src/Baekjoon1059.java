import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Baekjoon1059 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int l = Integer.parseInt(br.readLine());
        ArrayList<Integer> myArr = new ArrayList<>();
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);
        for(int i = 0; i < l; i++) {
            myArr.add(Integer.parseInt(st.nextToken()));
        }
        int n = Integer.parseInt(br.readLine());
        int start = 0, end = 1001;

        for(int i : myArr) {
            if(i < n) {
                if( i > start) {
                    start = i;
                }
            }else if(i > n) {
                if(i < end) {
                    end = i;
                }
            }else {
                System.out.println(0);
                return;
            }
        }

        int cnt = 0;

        for(int i = start + 1; i <= n; i++) {
            for(int j = n; j <= end - 1; j++) {
                cnt++;
            }
        }
        System.out.println(cnt-1);
    }
}
