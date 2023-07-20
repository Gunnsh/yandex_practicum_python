#A
print("".join(set(input())))

#B
print("".join(set(input()) & set(input())))

#C
num = int(input())
arr = set()
for i in range(num):
    arr = arr | set(input().split())
for i in arr:
    print(i)

#D
mannum = int(input())
ovsnum = int(input())
groupone = set()
grouptwo = set()
for i in range(1, mannum + ovsnum + 1):
    groupone.add(input()) if i <= mannum else grouptwo.add(input())
res = groupone & grouptwo
print("Таких нет") if res == set() else print(len(res))

#E
mannum = int(input())
ovsnum = int(input())
res = set()
for i in range(1, mannum + ovsnum + 1):
    res = res ^ {input()}
print("Таких нет") if res == set() else print(len(res))

#F
mannum = int(input())
ovsnum = int(input())
res = set()
for i in range(1, mannum + ovsnum + 1):
    res = res ^ {input()}
if res == set():
    print("Таких нет")
else:
    arr = list(res)
    arr.sort()
    print("\n".join(arr))

#G
text = input().upper()
morze = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}
for i in text:
    print() if i == " " else print(morze[i], end=" ")

#H
num = int(input())
arr = dict()
for i in range(num):
    string = input().split()
    for j in range(1, len(string)):
        if string[j] in arr:
            arr[string[j]].append(string[0])            
        else:
            arr[string[j]] = [string[0]]
res = arr.get(input(), "Таких нет")
if type(res) is str:
    print(res)
else:
    res.sort()
    [print(i) for i in res]

#I
arr = dict()
while (text := input()) != "":
    string = text.split()
    for j in range(len(string)):
        if string[j] in arr:
            arr[string[j]] = arr[string[j]] + 1            
        else:
            arr[string[j]] = 1
[print(key, value) for key, value in arr.items()]

#J
dict = {
    "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D",
    "Е": "E", "Ё": "E", "Ж": "Zh", "З": "Z", "И": "I",
    "Й": "I", "К": "K", "Л": "L", "М": "M", "Н": "N",
    "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T",
    "У": "U", "Ф": "F", "Х": "Kh", "Ц": "Tc", "Ч": "Ch",
    "Ш": "Sh", "Щ": "Shch", "Ы": "Y", "Э": "E", "Ю": "Iu",
    "Я": "Ia", "Ъ": "", "Ь": ""
}
text = input()
for i in text:
    if i.isalpha() and i.upper() in dict:
        if i.isupper():
            print(dict[i], end="")
        else:
            print(dict[i.upper()].lower(), end="")
    else:
        print(i, end="")

#K
num = int(input())
arr = dict()
res = 0
for i in range(num):
    name = input()
    if name not in arr:
        arr[name] = 1
    else:
        arr[name] += 1
res = sum([arr[i] for i in arr if arr[i] > 1])
print(res)

#L
num = int(input())
arr = dict()
res = 0
flag = True
array = []
for i in range(num):
    name = input()
    if name not in arr:
        arr[name] = 1
    else:
        arr[name] += 1
        flag = False
if flag is True:
    print("Однофамильцев нет")
else:
    for key, value in arr.items():
        if value > 1:
            array.append(f"{key} - {value}")
array.sort()
[print(i) for i in array]

#M
num = int(input())
food = set()
for i in range(num):
    food.add(input())

week = set()
days = int(input())
for i in range(days):
    numtoday = int(input())
    for j in range(numtoday):
        text = input()
        if text not in week:
            week.add(text)

res = list(food - week)
if res == []:
    print("Готовить нечего")
else:
    res.sort()
    [print(i) for i in res]

#N
foodnum = int(input())
foods = {input() for i in range(foodnum)}

candone = list()
recepts = int(input())
for i in range(recepts):
    receptname = input()
    foodneed = int(input())
    arr = {input() for j in range(foodneed)}
    if arr <= foods:
        candone.append(receptname)

if candone == list():
    print("Готовить нечего")
else:
    candone.sort()
    [print(i) for i in candone]

#O
text = [int(i) for i in input().split()]
result = list()
for i in text:
    num = bin(i)[2:]
    idict = dict()
    idict["digits"] = len(num)
    idict["units"] = str(num).count("1")
    idict["zeros"] = str(num).count("0")
    result.append(idict)
print(result)

#P
res = set()
while (text := input().split()) != []:
    for i in range(len(text)):
        if text[i] == "зайка":
            if i != 0:
                res = {text[i - 1]} | res
            if i != (len(text) - 1):
                res = {text[i + 1]} | res
{print(i) for i in res}

#Q
array = dict()
while (text := input().split()) != []:
    for i in range(len(text)):
        if text[0] not in array:
            array[text[0]] = {text[1]}
        else:
            array[text[0]].add(text[1])
        text.reverse()
for key, values in sorted(array.items()):
    new = set()
    for i in values:
        new = (new | array[i]) - {key}
    new = list(new - values)
    new.sort()
    print(f"{key}:", ", ".join(new))

#R
num = int(input())
arr = {}
for i in range(num):
    x, y = map(int, input().split())
    x //= 10
    y //= 10
    if (x, y) in arr.keys():
        arr[(x, y)] += 1
    else:
        arr[(x, y)] = 1
print(max(arr.values()))

#S
n = int(input())
arr = []
uniq = {}
for i in range(n):
    text = input().split(":")
    arr.extend(list(set((text[1].strip()).split(", "))))
for i in arr:
    uniq[i] = uniq.get(i, 0) + 1
arr = [keys for keys, values in uniq.items() if values == 1]
arr.sort()
[print(i) for i in arr]

#T
text = list(set(input().split("; ")))
text = list(map(int, text))
text.sort()
text = tuple(text)


def simplefunc(n, m):
    temp = set()
    temp1 = set()
    for i in range(1, n + 1):
        if n % i == 0:
            temp.add(i)
    for j in range(1, m + 1):
        if m % j == 0:
            temp1.add(j)
    return temp & temp1


for i in text:
    arr = list(text)
    arr.remove(i)
    res = []
    for j in arr:
        a = simplefunc(i, j)
        if a == {1}:
            res.append(j)
    if res != []:
        print(i, "-", ", ".join(map(str, res)))