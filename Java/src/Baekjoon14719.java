import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon14719 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int top;
    static int topIdx;
    static int answer;
    static int start;
    static int count;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] blocks = new int[W];
        top = 0;
        topIdx = -1;
        for(int i=0; i<W; i++) {
            int high = Integer.parseInt(st.nextToken());
            if(high > top) {
                top = high;
                topIdx = i;
            }
            blocks[i] = high;
        }
        answer = 0;
        start = blocks[0];
        count = 0;

        for(int i=0; i<=topIdx; i++) {
            if(blocks[i] >= start) {
                answer += count;
                start = blocks[i];
                count = 0;
            }
            else {
                count += start-blocks[i];
            }
        }
        start = blocks[W-1];
        count = 0;
        for(int i=W-1; topIdx<=i; i--) {
            if(blocks[i] >= start) {
                answer += count;
                start = blocks[i];
                count = 0;
            }
            else {
                count += start-blocks[i];
            }
        }
        System.out.println(answer);
    }
}
