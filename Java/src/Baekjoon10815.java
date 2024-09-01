import java.io.*;
import java.util.*;

public class Baekjoon10815 {

    static int N, M;
    static int[] nums;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);
        M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for (int i=0; i<M; i++) {
            int num = Integer.parseInt(st.nextToken());
            bw.write(binarySearch(num) + " ");
        }
        bw.flush();
        br.close();
        bw.close();

    }

    static int binarySearch(int num) {

        int start = 0;
        int end = N-1;

        while (start <= end) {
            int middle = (start + end) / 2;
            if (nums[middle] < num) {
                start = middle + 1;
            } else if (nums[middle] > num) {
                end = middle -1;
            } else {
                return 1;
            }
        }
        return 0;

    }
}
