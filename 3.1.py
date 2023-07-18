#A
num = int(input())
a = ("А", "а", "Б", "б", "В", "в")
flag = True

for i in range(1, num + 1):
    text = input()
    if text.startswith(a) is False:
        print("NO")
        flag = False
        break

if flag is True:
    print("YES")

#B
text = input()
i = 0
a = len(text)
while i <= (a - 1):
    print(text[i])
    i = i + 1

#C
head = int(input())
quantity = int(input())
res = []

for i in range(quantity):
    text = input()
    if len(text) <= head:
        res.append(text)
    else:
        cut = head - 3
        res.append(text[0:cut] + "...")

for i in range(quantity):
    print(res[i])

#D
while (text := input()) != "":
    if text[-3:] == "@@@":
        continue
    elif text[:2] == "##":
        print(text.strip("@#"))
    else:
        print(text)

#E
if (text := input()) == text[::-1]:
    print("YES")
else:
    print("NO")

#F
num = int(input())
n = 0

for i in range(num):
    text = input()
    n = n + text.count("зайка")

print(n)

#G
list = input().split()
print(int(list[0]) + int(list[1]))

#H
num = int(input())
res = []
for i in range(num):
    first = input().find("зайка") + 1
    if first == 0:
        res.append("Заек нет =(")
    else:
        res.append(first)
    
for i in range(len(res)):
    print(res[i])

#I
while (text := input()) != "":
    index = text.find("#")
    if text[0] == "#":
        continue
    elif index > 0:
        print(text[:index])
    else:
        print(text)

#J
string = ""
countend = 0
resend = 0

while (text := input()) != "ФИНИШ":
    string += text.lower()

arr = list(string)
arr.sort()
arr.reverse()

while arr != []:
    count = arr.count(arr[0])
    res = arr[0]
    if count >= countend and arr[0] != " ":
        resend = res
        countend = count
    while arr.count(res) != 0:
        arr.remove(res)

print(resend)

#K
num = int(input())
arr = []
string = ""

for i in range(num):
    arr.append(input())

search = input().lower()

for j in range(len(arr)):
    string = str(arr[j]).lower()
    if string.find(search) >= 0:
        print(arr[j])

#L
num = int(input())
arr = [
    "Манная",
    "Гречневая",
    "Пшённая",
    "Овсяная",
    "Рисовая"]
count = 1
for i in range(num):
    if count % 5 == 0:
        print(arr[count - 1])
        count = 1
    else:
        print(arr[count - 1])
        count += 1

#M
num = int(input())
arr = []

for i in range(num):
    arr.append(int(input()))
ast = int(input())
for j in range(len(arr)):
    print(arr[j] ** ast)

#N
num = input().split()
ast = int(input())

for i in range(len(num)):
    print(int(num[i]) ** ast, end=" ")

#O
array = input().split()
res = 1

for i in range(2, int(min(array)) + 1):
    index = 0
    minres = []
    flag = True
    alg = 0
    while index < len(array):
        if int(array[index]) % i == 0:
            alg = int(array[index]) / i
        else:
            flag = False
        minres.append(int(alg))
        index += 1
    if flag is True:
        res = i

print(res)

#P
leng = int(input())
num = int(input())
array = []
genleng = 0
flag = False

for i in range(num):
    str = input()
    if flag is True:
        continue
    if (genleng + len(str) + 3) >= leng:
        array.append(str[:leng - genleng - 3] + "...")
        flag = True
    else:
        if flag is True:
            continue
        array.append(str)
        genleng += len(str)

for i in range(len(array)):
    print(array[i])

#Q
string = input().lower()

string = string.replace(" ", "")
arr = list(string)
arr.reverse()
if list(string) == arr:
    print("YES")
else:
    print("NO")

#R
text = list(input())
num = text[0]
count = 0

while text != []:
    if num == text[0]:
        num = text[0]
        count += 1
        text.remove(text[0])
    else:
        print(num, str(count))
        num = text[0]
        count = 0
print(num, str(count))

#S
s = [x for x in input().split()]
stack = []
for x in s:
    if x in "*+-":
        b = stack.pop()
        a = stack.pop()
        stack.append(eval(f"{a} {x} {b}"))
    else:
        stack.append(x)
print(*stack)

#T
s = [x for x in input().split()]
stack = []
for x in s:
    if x in "*+-/":
        b = stack.pop()
        a = stack.pop()
        if x == "/":
            x = "//"
        stack.append(int(eval(f"{a} {x} {b}")))
    elif x in "~":
        a = stack.pop()
        stack.append(int(a) * -1)
    elif x in "!":
        a = 1
        for i in range(1, int(stack.pop()) + 1):
            a *= i
        stack.append(str(a))
    elif x in "#":
        a = stack.pop()
        stack.extend([a, a])
    elif x in "@":
        c = stack.pop()
        b = stack.pop()
        a = stack.pop()
        stack.extend([b, c, a])
    else:
        stack.append(x)
print(*stack)