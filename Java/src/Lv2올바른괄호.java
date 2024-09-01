class Lv2올바른괄호 {
    boolean solution(String s) {
        boolean answer = true;
        int openParenthesis = 0;

        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) =='(') {
                openParenthesis++;
                continue;
            }
            openParenthesis--;
            if (openParenthesis < 0) {
                answer = false;
                break;
            }
        }
        if (openParenthesis != 0) answer = false;

        return answer;
    }
}