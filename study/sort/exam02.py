N = int(input())
words = [input() for _ in range(N)]

words = sorted(words)
for word in words:
    print(word)
