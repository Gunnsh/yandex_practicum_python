#A
name = input("Как Вас зовут?\n")
print(f"Здравствуйте, {name}!")
que = input("Как дела?\n")
if que == "хорошо":
    print("Я за вас рада!")
else:
    print("Всё наладится!")

#B
petr = int(input())
vas = int(input())
if petr > vas:
    print("Петя")
else:
    print("Вася")

#C
petr = int(input())
vas = int(input())
tol = int(input())

if petr > vas and petr > tol:
    print("Петя")
elif vas > petr and vas > tol:
    print("Вася")
else:
    print("Толя")

#D
petr = int(input())
vas = int(input())
tol = int(input())

if petr > vas and petr > tol:
    first = "Петя"
    if vas > tol:
        second = "Вася"
        third = "Толя"
    else:
        second = "Толя"
        third = "Вася"
elif vas > petr and vas > tol:
    first = "Вася"
    if petr > tol:
        second = "Петя"
        third = "Толя"
    else:
        second = "Толя"
        third = "Петя"
else:
    first = "Толя"
    if petr > vas:
        second = "Петя"
        third = "Вася"
    else:
        second = "Вася"
        third = "Петя"

print(f"1. {first}")
print(f"2. {second}")
print(f"3. {third}")

#E
n = int(input())
m = int(input())

petr = 4 + n
vas = 3 + m

if petr > vas:
    print("Петя")
else:
    print("Вася")

#F
year = int(input())
four = year % 4
hun = year % 100
forhun = year % 400
if forhun == 0:
    print("YES")
elif hun == 0:
    print("NO")
elif four == 0:
    print("YES")
else:
    print("NO")

#G
num = input()
enum = num[-1] + num[-2] + num[-3] + num[-4]
if enum == num:
    print("YES")
else:
    print("NO")

#H
text = input()
if "зайка" in text:
    print("YES")
else:
    print("NO")

#I
name1 = input()
name2 = input()
name3 = input()

print(min(name1, name2, name3))

#J
num = input()
first = int(num[-1]) + int(num[-2])
second = int(num[-2]) + int(num[-3])
print(str(max(first, second)) + str(min(first, second)))

#K
num = input()
maxn = 0
minn = 0
ave = 0

fi = int(num[0])
se = int(num[1])
th = int(num[2])

inmax = int(max(num))
inmin = int(min(num))

if inmax == fi:
    maxn = fi
    if inmin == se:
        minn = se
        ave = th
    else:
        minn = th
        ave = se
elif inmax == se:
    maxn = se
    if inmin == fi:
        minn = fi
        ave = th
    else:
        minn = th
        ave = fi
else:
    maxn = th
    if inmin == fi:
        minn = fi
        ave = se
    else:
        minn = se
        ave = fi
    
if minn + maxn == ave * 2:
    print("YES")
else:
    print("NO")

#L
first = int(input())
second = int(input())
third = int(input())

if first + second > third:
    if first + third > second:
        if third + second > first:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
    

#M
elf = input()
gnom = input()
human = input()

if elf[0] == gnom[0] == human[0]:
    print(elf[0])
elif elf[1] == gnom[1] == human[1]:
    print(elf[1])

#N
num = input()
maxn = 0
minn = 0
ave = 0

fi = int(num[0])
se = int(num[1])
th = int(num[2])

inmax = int(max(num))
inmin = int(min(num))

if inmax == fi:
    maxn = fi
    if inmin == se:
        minn = se
        ave = th
    else:
        minn = th
        ave = se
elif inmax == se:
    maxn = se
    if inmin == fi:
        minn = fi
        ave = th
    else:
        minn = th
        ave = fi
else:
    maxn = th
    if inmin == fi:
        minn = fi
        ave = se
    else:
        minn = se
        ave = fi

res = str(maxn) + str(ave)

if minn != 0:
    print(minn, ave, " ", res, sep="")
else:
    print(ave, minn, " ", res, sep="")

#O
first = input()
second = input()

firstmax = max(first)
firstmin = min(first)
secondmax = max(second)
secondmin = min(second)

ave1 = 0
ave2 = 0

allmax = max(firstmax, secondmax)
allmin = min(firstmin, secondmin)

if allmax == firstmax:
    ave1 = secondmax
else:
    ave1 = firstmax

if allmin == firstmin:
    ave2 = secondmin
else:
    ave2 = firstmin

ave = str(int(ave1) + int(ave2))

print(allmax, ave[-1], allmin, sep="")

#P
petr = int(input())
vas = int(input())
tol = int(input())

if petr > vas and petr > tol:
    first = "Петя"
    if vas > tol:
        second = "Вася"
        third = "Толя"
    else:
        second = "Толя"
        third = "Вася"
elif vas > petr and vas > tol:
    first = "Вася"
    if petr > tol:
        second = "Петя"
        third = "Толя"
    else:
        second = "Толя"
        third = "Петя"
else:
    first = "Толя"
    if vas > petr:
        second = "Вася"
        third = "Петя"
    else:
        second = "Петя"
        third = "Вася"

print(f"{first:>14}")
print(f"{second:>6}")
print(f"{third:>22}")
print("   II      I      III ")

#Q
a = float(input())
b = float(input())
c = float(input())  
if a == 0:
    if b == 0 and c == 0:
        print("Infinite solutions")
    if b != 0 and (c != 0 or c == 0):
        x1 = -(c / b)
        print(round(x1, 2))
    if b == 0 and c != 0:
        print("No solution")
else:
    D = ((b) ** 2) - (4 * a * c)
    if D > 0:
        x2 = ((-b) - (D ** 0.5)) / (2 * a)
        x3 = ((-b) + (D ** 0.5)) / (2 * a)
        if x2 < x3:
            x3, x2 = x2, x3
        print(round(x3, 2), round(x2, 2))
    elif D == 0:
        x4 = (-b) / (2 * a)
        print(round(x4, 2))
    elif D < 0:
        print("No solution")

#R
a = int(input())
b = int(input())
c = int(input())

aa = b ** 2 + c ** 2 - a ** 2
bb = a ** 2 + c ** 2 - b ** 2
cc = a ** 2 + b ** 2 - c ** 2

if aa == 0 or bb == 0 or cc == 0:
    print("100%")
elif aa < 0 or bb < 0 or cc < 0:
    print("велика")
else:
    print("крайне мала")

#S
x = float(input())
y = float(input())
r = 10
if x ** 2 + y ** 2 > r ** 2:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
elif y >= 0 and x >= 0 and (x ** 2 + y ** 2 <= 25):
    print('Опасность! Покиньте зону как можно скорее!')
elif (x - 5) * (x + 7) <= 4 * y and y < 0:
    print('Опасность! Покиньте зону как можно скорее!')
elif x <= 0 and y >= 0 and y <= 1.6 * x + 11 and y <= 5:
    print('Опасность! Покиньте зону как можно скорее!')
else:
    print('Зона безопасна. Продолжайте работу.')

#T
str1 = input()
str2 = input()
str3 = input()

if str1 >= str2 and str1 >= str3:
    maxs = str1
    if str2 > str3:
        ave = str2
        mins = str3
    else:
        ave = str3
        mins = str2
elif str2 >= str1 and str2 >= str3:
    maxs = str2
    if str1 > str3:
        ave = str1
        mins = str3
    else:
        ave = str3
        mins = str1
else:
    maxs = str3
    if str2 > str1:
        ave = str2
        mins = str1
    else:
        ave = str1
        mins = str2

if 'зайка' in mins:
    print(mins, len(mins))
elif 'зайка' in ave:
    print(ave, len(ave))
elif 'зайка' in maxs:
    print(maxs, len(maxs))