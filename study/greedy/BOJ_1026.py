N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sorted_a = sorted(A)
sorted_b = sorted(B, reverse=True)

result = 0
for a, b in zip(sorted_a, sorted_b):
    result += a * b
print(result)
