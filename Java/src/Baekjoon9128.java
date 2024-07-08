import java.io.*;
import java.util.*;

public class Baekjoon9128 {

    static int T;
    static int n;
    static long[][] customers;
    static long x;
    static long y;
    static long totalX;
    static long totalY;
    static double total;
    static long north;
    static long south;
    static long east;
    static long west;
    static long house;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        T = Integer.parseInt(br.readLine());
        for (int i=0; i<T; i++) {
            n = Integer.parseInt(br.readLine());
            customers = new long[n][2];
            for (int j=0; j<n; j++) {
                st = new StringTokenizer(br.readLine());
                customers[j][0] = Integer.parseInt(st.nextToken());
                customers[j][1] = Integer.parseInt(st.nextToken());
            }

            long tmpX = 0;
            long tmpY = 0;
            for (int j=0; j<n; j++) {
                tmpX += customers[j][0];
                tmpY += customers[j][1];
            }
            x = tmpX / n;
            y = tmpY / n;

            total = checkDistance(x, y);
            String formattedTotal = String.format("%.0f", total);
            System.out.println(formattedTotal);
            east = findEndX(2000000000, x, y);
//            west = findEndX(-1000000000, x, y);
            north = findEndY(2000000000, x, y);
//            south = findEndY(-1000000000, x, y);
            double high = Math.ceil(east-x);
            double low = Math.ceil(x-east);
            double cha = high - low;
            if (((int) cha%2) == 0) {
                house = (((east-x)*2+1)*((north-y)*2+1))/2;
            } else {
                house = (east-x)*(east-x)*4;
            }
            System.out.println(house);
            for(int j=0; j<n; j++) {
                if (checkDistance(customers[j][0], customers[j][1]) == total) house -= 1;
            }
            System.out.println(east);
            System.out.println(north);
            System.out.println(house);
            if (east > 1000000000) house -= (east-1000000000)*(east-1000000000);
            if (north > 1000000000) house -= (north-1000000000)*(north-1000000000);
            if (x-east < -1000000000) house -= (Math.abs(x-east) - 1000000000) * (Math.abs(x-east) - 1000000000);
            if (x-north < -1000000000) house -= (Math.abs(x-north) - 1000000000) * (Math.abs(x-north) - 1000000000);

            System.out.println(house);
        }
    }
    static double checkDistance(long x, long y) {
        long tmpX = 0;
        long tmpY = 0;
        for(int j=0; j<n; j++) {
            tmpX += Math.abs(customers[j][0] - x);
            tmpY += Math.abs(customers[j][1] - y);
        }
        return Math.ceil(tmpX + tmpY);
    }

    static long findEndX(long targetX, long x, long y) {
        if (checkDistance(targetX, y) == total) return targetX;
        if (checkDistance(targetX, y) > total) return findEndX((targetX+x)/2 - 1, x, y);
        return findEndX(targetX, (targetX+x)/2 + 1, y);
    }

    static long findEndY(long targetY, long x, long y) {
        if (checkDistance(x, targetY) == total) return targetY;
        if (checkDistance(x, targetY) > total) return findEndY((targetY+y)/2 - 1, x, y);
        return findEndY(targetY, x, (targetY+x)/2 + 1);
    }
}
