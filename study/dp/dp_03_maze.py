N, M = map(int, input().split())

arr = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
print(arr)
