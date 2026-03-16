from itertools import permutations


def check_strike_ball(target_a, target_b):
    strike = 0
    ball = 0
    for i in range(3):
        for j in range(3):
            if target_a[i] == int(target_b[j]):
                if i == j:
                    strike += 1
                else:
                    ball += 1
    return strike, ball


N = int(input())
hint_list = [input().split() for _ in range(N)]
candidates = list(permutations(range(1, 10), 3))
for hint in hint_list:
    num, hint_strike, hint_ball = hint[0], int(hint[1]), int(hint[2])
    candidates = [cur for cur in candidates if (hint_strike, hint_ball) == check_strike_ball(cur, num)]

print(len(candidates))
