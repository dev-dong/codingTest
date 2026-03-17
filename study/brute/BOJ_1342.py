S = list(input())
result = set()
check = [False] * len(S)
origin_str = []
choose = []


def search(lev):
    if lev == len(S):
        result.add(''.join(choose))
        return
    for i in range(len(S)):
        if check[i]:
            continue
        if choose and choose[-1] == S[i]:
            continue
        choose.append(S[i])
        check[i] = True
        search(lev + 1)
        choose.pop()
        check[i] = False


search(0)
print(len(result))
