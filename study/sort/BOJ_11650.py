N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
sorted_nums = sorted(nums, key=lambda x: (x[0], x[1]))
for sorted_num in sorted_nums:
    print(' '.join(map(str, sorted_num)))
