class Plv2연속된부분수열의합 {
    public int[] solution(int[] sequence, int k) {
        int lenFix = sequence.length;
        int resultLeft = 0;
        int resultRight = lenFix;
        int L = 0;
        int R = 0;
        int total = sequence[0];

        while(L<=R) {

            if(total == k) {
                if(resultRight - resultLeft > R-L) {
                    resultLeft = L;
                    resultRight = R;
                }
                R++;
                if(R==lenFix) {
                    break;
                }
                total += sequence[R];
            }
            else if (total > k) {
                total -= sequence[L];
                L++;
            }
            else {
                R++;
                if(R==lenFix){
                    break;
                }
                total += sequence[R];
            }
        }

        int[] answer = {resultLeft, resultRight};
        return answer;
    }
}