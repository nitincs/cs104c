import java.io.*;
import java.util.*;

// Runs in 0.46 seconds
public class FCTRL_BufferedReader {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int numCases = Integer.parseInt(bufferedReader.readLine());
        for (int i = 0; i < numCases; i++) {
            int n = Integer.parseInt(bufferedReader.readLine());

            int ans = 0;
            for (int j = 5; j <= n; j *= 5) {
                ans += n / j;
            }

            System.out.println(ans);
        }
    }
}
