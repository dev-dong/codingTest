vowels = ['a', 'e', 'i', 'o', 'u']
choose = []


def to_string(params):
    return "".join(params)


def combination(index, level):
    if level == input_list[0]:
        vowel_count = sum(1 for c in choose if c in vowels)
        consonant_count = len(choose) - vowel_count
        if vowel_count >= 1 and consonant_count >= 2:
            print(to_string(choose))
        return
    for i in range(index, input_list[1]):
        choose.append(str_list[i])
        combination(i + 1, level + 1)
        choose.pop()


input_list = list(map(int, input().split()))
str_list = input().split()
str_list.sort()
combination(0, 0)
