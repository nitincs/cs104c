# Python 3
# Use raw_input and a single / for division for python 2

def main():
    num_cases = int(input())
    for _ in range(num_cases):
        n = int(input())
        d = 5
        ans = 0
        while d <= n:
            ans += n // d
            d *= 5

        print(ans)


main()
