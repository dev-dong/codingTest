N, S = map(int, input().split())
arr = list(map(int, input().split()))
result = []
choose = []


def search(lev):
    if lev == N:
        if choose and sum(choose) == S:
            result.append(choose[:])
        return
    choose.append(arr[lev])
    search(lev + 1)
    choose.pop()
    search(lev + 1)


search(0)
print(len(result))
