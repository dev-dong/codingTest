N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for col in range(3)] for row in range(N)]
dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]
result = 0
for i in range(1, N):
    dp[i][0] = arr[i][0] + min(dp[i - 1][1], dp[i - 1][2])  # R
    dp[i][1] = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2])  # G
    dp[i][2] = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1])  # B

print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))
