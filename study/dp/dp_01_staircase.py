N = int(input())
dp = [0] * (N + 1)

dp[1] = 1
dp[2] = 2
# 4 = dp[0] + dp[0] + dp[0] + dp[0]
# 4 = dp[0] + dp[0] + dp[1]
# 4 = dp[0] + dp[1] + dp[0]
# 4 = dp[1] + dp[0] + dp[0]
# 4 = dp[1] + dp[1]

# (i-1)번째 계단에서 1칸 올라오기
# (i-2)번째 계단에서 2칸 올라오기
# dp[1] = i가 3
# dp[2] = i가 4
for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[N])
