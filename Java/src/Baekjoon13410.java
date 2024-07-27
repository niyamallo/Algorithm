    import java.io.*;
    import java.util.*;

    public class Baekjoon13410 {
    
        static int N;
        static int K;

        public static void main(String[] args) throws IOException {

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            int max = Integer.MIN_VALUE;

            for (int i=1; i<K+1; i++) {
                int temp = N * i;
                String tempString = String.valueOf(temp);
                StringBuilder sb = new StringBuilder();
                for (int j=tempString.length()-1; j>=0; j--) {
                    sb.append(tempString.charAt(j));
                }

                max = Math.max(max, Integer.parseInt(sb.toString()));
            }

            System.out.println(max);
        }
    }
