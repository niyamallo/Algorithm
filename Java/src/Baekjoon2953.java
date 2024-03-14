import java.util.Scanner;

public class Baekjoon2953 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int winnerNumber = 0;
        int maxScore = 0;
        for(int i = 0; i < 5; i++) {
            String scores = scanner.nextLine();
            String[] scoreArray = scores.split(" ");

            int totalScore = 0;
            for (String score : scoreArray) {
                totalScore += Integer.parseInt(score);
            }

            if (totalScore > maxScore) {
                maxScore = totalScore;
                winnerNumber = i + 1;
            }
        }
        System.out.println(winnerNumber + " " + maxScore);
    }
}
