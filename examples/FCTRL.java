import java.io.*;
import java.util.*;

// Runs in 0.63 seconds on SPOJ
public class FCTRL {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        int numCases = scan.nextInt();
        for (int i = 0; i < numCases; i++) {
            int n = scan.nextInt();

            int ans = 0;
            for (int j = 5; j <= n; j *= 5) {
                ans += n / j;
            }

            System.out.println(ans);
        }
    }
}
