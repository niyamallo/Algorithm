import java.util.Scanner;

public class Baekjoon1264 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            String str = scanner.nextLine();
            str = str.toLowerCase();
            int count = 0;
            if (str.equals("#")) {
                break;
            } else {
                for (int i = 0; i < str.length(); i++) {
                    char s = str.charAt(i);
                    if (s == 'a' | s =='e' | s == 'i' | s =='o' | s == 'u') {
                        count += 1;
                    }
                }
            }
            System.out.println(count);
        }
    }
}
