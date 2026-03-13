def combination(index, level):
    if level == 6:
        for i in choose:
            print(i, end=' ')
        print()
        return

    for i in range(index, len(num_list)):
        choose.append(num_list[i])
        combination(i + 1, level + 1)
        choose.pop()


while True:
    input_list = list(map(int, input().split()))
    num_list = input_list[1:]
    choose = []
    if input_list[0] == 0:
        break
    combination(0, 0)
    print()
