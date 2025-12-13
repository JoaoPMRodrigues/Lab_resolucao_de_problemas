import sys


def main():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)

    N = int(next(it))

    m = [[0] * (N + 1) for _ in range(N + 1)]
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            m[i][j] = int(next(it))
            dp[i][j] = 0

    for i in range(1, N + 1):
        base = 0
        for j in range(1, N + 1):
            base += m[i][j]
            if j > i:
                base -= m[i][j - i]
            if j >= i:
                dp[i][j] = base
                if i > 1:
                    dp[i][j] += min(dp[i - 1][j], dp[i - 1][j - 1])

    print(dp[N][N])


if __name__ == "__main__":
    main()
