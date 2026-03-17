N = int(input())
money = 1000 - N
coins = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coins:
    count += money // coin
    money = money % coin

print(count)
