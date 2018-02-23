def f(t, x, k):
    return t * (t - 1) // 2 + k * (t // x)

def main():
    n, x, k = map(int, input().split())
    lo = 0
    hi = n
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if f(mid, x, k) <= n:
            lo = mid
        else:
            hi = mid

    print(lo)

t = int(input())
for _ in range(t):
    main()
