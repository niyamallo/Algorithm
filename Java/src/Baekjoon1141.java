import java.io.*;
import java.util.*;

public class Baekjoon1141 {

    static int N;
    static String[] strings;
    static List<String> nonPrefix;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        strings = new String[N];
        for (int i=0; i<N; i++) {
            strings[i] = br.readLine();
        }

        Arrays.sort(strings, (str1, str2) -> str2.length() - str1.length());

        nonPrefix = new LinkedList<>();

        for (String str : strings) {
            if (nonPrefix.isEmpty()) {
                nonPrefix.add(str);
                continue;
            }

            boolean isPrefix = false;

            for (String nonPre : nonPrefix) {
                if (nonPre.indexOf(str) == 0) {
                    isPrefix = true;
                    break;
                }
            }

            if (!isPrefix) {
                nonPrefix.add(str);
            }
        }

        System.out.println(nonPrefix.size());
    }
}
