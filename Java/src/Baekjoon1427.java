import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Baekjoon1427 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String strNum = br.readLine();
        int lenNum = strNum.length();
        int[] A = new int[lenNum];
        for(int i=0; i<lenNum; i++) {
            A[i] = Integer.parseInt(strNum.substring(i,i+1));
        }

        for(int i=0; i<lenNum; i++) {
            int maxIdx = i;
            for(int j=i+1; j<lenNum; j++) {
                if (A[j]>A[maxIdx]) {
                    maxIdx = j;
                }
            }
            int tmp = A[i];
            A[i] = A[maxIdx];
            A[maxIdx] = tmp;
        }
        for(int i=0; i<lenNum; i++) {
            bw.write(String.valueOf(A[i]));
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
