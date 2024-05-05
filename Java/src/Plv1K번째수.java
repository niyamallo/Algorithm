import java.util.Arrays;

class Plv1K번째수 {
    static int i;
    static int j;
    static int k;
    int[] newArr;

    public int[] solution(int[] array, int[][] commands) {
        int len = commands.length;
        int[] answer = new int[len];
        for(int c=0; c<len; c++) {
            i = commands[c][0];
            j = commands[c][1];
            k = commands[c][2];
            newArr = new int[j-i+1];
            for(int n=0; n<j-i+1; n++) {
                newArr[n] = array[n+i-1];
            }
            Arrays.sort(newArr);
            answer[c] = newArr[k-1];
        }

        return answer;
    }
}