N = int(input())
input_numbers = [list(map(int, input().split())) for _ in range(N)]
sorted_numbers = sorted(input_numbers, key=lambda x: (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))

for number in sorted_numbers[:3]:
    print(number[0], end=' ')
