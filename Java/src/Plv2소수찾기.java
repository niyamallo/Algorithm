import java.util.HashSet;
import java.util.Set;

class Plv2소수찾기 {
    static Set<Integer> set;
    static int len;
    static boolean[] visited;
    static int count;
    static boolean[] primes;

    public int solution(String numbers) {
        set = new HashSet<>();
        len = numbers.length();
        visited = new boolean[len];
        count = 0;
        primes = new boolean[10000000];
        notPrime();

        setNums(numbers, "", 0);
        for(int i: set) {
            if(!primes[i]) {
                count++;
            }
        }

        int answer = count;
        return answer;
    }
    private static void setNums(String numbers, String s, int depth) {
        if(depth>len){
            return;
        }
        for(int i=0; i<len; i++) {
            if(!visited[i]) {
                visited[i] = true;
                String str = s + numbers.substring(i,i+1);
                set.add(Integer.parseInt(str));
                setNums(numbers, str, depth+1);
                visited[i] = false;
            }
        }
    }
    private static void notPrime() {
        primes[0] = true;
        primes[1] = true;
        for(int i=2; i<=Math.sqrt(10000000); i++) {
            if(!primes[i]) {
                for(int j=i+i; j<10000000; j+=i) {
                    primes[j] = true;
                }
            }
        }
    }
}
