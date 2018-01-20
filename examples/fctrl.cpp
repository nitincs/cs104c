#include <iostream>

using namespace std;

int main() {
    // The following two lines speed up cin, but aren't strictly necessary.
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int num_cases;
    cin >> num_cases;

    int n;
    while (num_cases-- > 0) {
        cin >> n;
        int ans = 0;

        for (int d = 5; d <= n; d *= 5) {
            ans += n / d;
        }

        cout << ans << '\n';
    }

    return 0;
}
