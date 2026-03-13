N = int(input())
lst = list(range(1, N + 1))
check = [False] * N
choose = []


def permutation(level):
    if level == N:
        for c in choose:
            print(c, end=' ')
        print()
        return
    for i in range(0, N):
        if check[i]:
            continue
        choose.append(lst[i])
        check[i] = True
        permutation(level + 1)
        check[i] = False
        choose.pop()


permutation(0)
