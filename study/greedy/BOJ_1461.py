N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))
max_num = abs(max(arr, key=abs))
minus_arr = sorted([abs(x) for x in arr if x < 0], reverse=True)
plus_arr = sorted([x for x in arr if x > 0], reverse=True)

ans = 0
for i in range(0, len(minus_arr), M):
    ans += abs(minus_arr[i]) * 2
for j in range(0, len(plus_arr), M):
    ans += plus_arr[j] * 2
ans = ans - max_num
print(ans)
