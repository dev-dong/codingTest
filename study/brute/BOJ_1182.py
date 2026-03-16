answer = 0
# total_sum = sum(list(map(int, input().split())))
input_list = list(map(int, input().split()))
result = []
choose = []

def combination(index, level):
    if index == level:
        result.append(choose[:])
        return
    for i in range(index, len(input_list)):
        choose.append(input_list[i])
        combination(i + 1, level)
        choose.pop()

for lvl in range(1, len(input_list) + 1):
    combination(0, lvl)

print(result)

