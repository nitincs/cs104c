#include <cstdio>

using namespace std;

int main() {
    int num_cases;
    scanf("%d", &num_cases);

    int n;
    while (num_cases-- > 0) {
        scanf("%d", &n);
        int ans = 0;

        for (int d = 5; d <= n; d *= 5) {
            ans += n / d;
        }

        printf("%d\n", ans);
    }

    return 0;
}
