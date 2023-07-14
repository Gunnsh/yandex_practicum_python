#A
num = int(input())

for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(j * i, end=" ")
    print("")

#B
num = int(input())

for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(f"{j} * {i}", "=", j * i)

#C
num = int(input())
flag = False
k = 1
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(k, end=" ")
        if k == num:
            flag = True
            break
        k = k + 1
    if flag:
        break
    print("")

#D
num = int(input())
res = 0
for i in range(num):
    ln = 0
    number = input()
    while ln <= (len(number) - 1):
        res += int(number[ln])
        ln += 1

print(res)

#E
num = int(input())
k = 0
field = ""

for i in range(num):
    while (text := input()) != 'ВСЁ':
        field = field + text
    if 'зайка' in field:
        k = k + 1
    field = ""

print(k)

#F
num = int(input())
array = []

for i in range(num):
    array.append(input())

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

#G
num = int(input())
b = 0

for i in range(num):
    b = 3 + i
    while b > 0:
        print(f"До старта {b} секунд(ы)")
        b -= 1
    i += 1
    print(f"Старт {i}!!!")

#H
num = int(input())
ressum = 0
resname = ""

for i in range(num):
    name = input()
    dig = input()
    sum = 0
    for i in range(len(dig)):
        sum += int(dig[i])
    if sum >= ressum:
        resname = name
        ressum = sum

print(name)

#I
num = int(input())
res = ""

for i in range(num):
    dig = input()
    res += max(dig)

print(res)

#J
num = int(input())
print("А Б В")
for i in range(1, num - 1):
    for j in range(1, num - i):
        print(i, j, num - i - j)

#K
num = int(input())
n = 0
flag = False

for i in range(num):
    dig = int(input())
    if dig == 1:
        n = n
    elif dig == 2:
        n += 1
    else:
        for k in range(2, dig):
            if dig % k == 0:
                flag = False
                break
            else:
                flag = True
        if flag:
            n += 1

print(n)

#L
ver = int(input())
gor = int(input())
n = 1

leng = len(str(ver * gor))
for i in range(ver):
    for j in range(gor):
        print(f"{n:>{leng}}", end=" ")
        n += 1
    print()

#M
ver = int(input())
gor = int(input())
n = 1

leng = len(str(ver * gor))
for i in range(ver):
    for j in range(gor):
            print(f"{n:>{leng}}", end=" ")
            n += ver
    print()
    n = i + 2

#N
ver = int(input())
gor = int(input())
n = 1
m = 1

leng = len(str(ver * gor))
for i in range(1, ver + 1):
    if i % 2 == 0:
        n += gor
        m = n - 1
    for j in range(1, gor + 1):
        if i % 2 == 0:
            print(f"{m:>{leng}}", end=" ")
            m -= 1
        else:
            print(f"{n:>{leng}}", end=" ")
            n += 1
            
    print()

#O
ver = int(input())
gor = int(input())

leng = len(str(ver * gor))
for i in range(1, ver + 1):
    for j in range(1, gor + 1):
        if j % 2 == 0:
            n = (ver * j) - i + 1
        else:
            n = (ver * (j - 1)) + i
        print(f"{n:>{leng}}", end=" ")
    print()

#P
ver = int(input())
gor = int(input())

leng = ver * gor + (ver - 1)
for i in range(1, ver + 1):
    for j in range(1, ver + 1):
        if j == 1:
            print(f"{i * j:^{gor}}", end="")
        else:
            print(f"|{i * j:^{gor}}", end="")
    print()
    if i != ver:
        print("-" * leng)

#Q
num = int(input())
one = ""
res = 0

for i in range(num):
    dig = input()
    for j in range((len(dig) - 1), -1, -1):
        one += dig[j]
    if dig == one:
        res += 1
    one = ""

print(res)

#R
num = int(input())
res = 0
flag = False
string = ""
leng = 0

for i in range(1, num + 1):
    for j in range(1, i + 1):
        res += 1
        string += str(res) + " "
        if res == num:
            flag = True
            break
    leng = len(string)
    string = ""
    if flag:
        break

flag = False
res = 0

for i in range(1, num + 1):
    for j in range(1, i + 1):
        res += 1
        string += str(res) + " "
        if res == num:
            flag = True
            break
    print(f"{string:^{leng}}")
    string = ""
    if flag:
        break

#S
n = int(input())
max_num = (n + 1) // 2
max_length = len(str(max_num))
for i in range(0, n // 2 + n % 2):
    num = 1
    length = len(str(num))
    for j in range(i):
        print(f"{' ' * (max_length - length)}{num}", end=" ")
        num += 1
        length = len(str(num))
    for j in range(n - 2 * i):
        print(f"{' ' * (max_length - length)}{num}", end=" ")
    num -= 1
    length = len(str(num))
    for j in range(i):
        print(f"{' ' * (max_length - length)}{num}", end=" ")
        num -= 1
        length = len(str(num))
    print()
for i in range(n // 2 - 1, -1, -1):
    num = 1
    length = len(str(num))
    for j in range(i):
        print(f"{' ' * (max_length - length)}{num}", end=" ")
        num += 1
        length = len(str(num))
    for j in range(n - 2 * i):
        print(f"{' ' * (max_length - length)}{num}", end=" ")
    num -= 1
    length = len(str(num))
    for j in range(i):
        print(f"{' ' * (max_length - length)}{num}", end=" ")
        num -= 1
        length = len(str(num))
    print()

#T
num = int(input())
sum = 0
res = 0
otvet = 0

for i in range(10, 1, -1):
    b = num
    while b > 0:
        if b % i == 0:
            b = b / i
        else:
            sum += (b - ((b // i) * i))
            b = b // i
    if sum >= res:
        res = sum
        otvet = i
    sum = 0

print(otvet)