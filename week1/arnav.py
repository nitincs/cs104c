# Python 3
def main():
    n, k = map(int, input().split())
    s = input()

    start = s.index('G')
    target = s.index('T')

    if start > target:
        start, target = target, start

    i = 1
    jumps = (target - start) // k
    valid = (target - start) % k == 0 and all(s[start + i * k] == '.' for i in range(1, jumps))

    print('YES' if valid else 'NO')

main()
