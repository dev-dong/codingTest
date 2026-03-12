N = 3
R = 2
lst = [1, 2, 3]
choose = []


def combination(index, level):
    if level == R:
        print(f"Combination found: {choose}")
        return

    for n in range(index, N):
        print(f"index: {n}, level: {level}, choose: {choose}")
        choose.append(lst[n])
        combination(n + 1, level + 1)
        print(f"pop call index: {n}, level: {level}")
        choose.pop()


combination(0, 0)
