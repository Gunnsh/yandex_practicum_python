#A
while input() != 'Три!':
    print('Режим ожидания...')
print('Ёлочка, гори!')

#B
n = 0
name = input()
while name != 'Приехали!':
    if 'зайка' in name:
        n = n + 1
    name = input()

print(n)

#C
begin = int(input())
end = int(input())

for i in range(begin, end + 1):
    print(i, end=" ")

#D
begin = int(input())
end = int(input())

if end < begin:
    n = -1
else:
    n = 1

for i in range(begin, end + n, n):
    print(i, end=" ")

#E
check = 0
cost = float(input())
while cost != 0:
    if cost >= 500:
        cost = cost - (cost / 10)
    check = check + cost
    cost = float(input())

print(check)

#F
num1 = int(input())
num2 = int(input())

maxn = max(num1, num2)
minn = min(num1, num2)

while maxn % minn != 0:
    n = maxn % minn
    maxn = minn
    minn = n

print(n)

#G
num1 = int(input())
num2 = int(input())

maxn = max(num1, num2)
minn = min(num1, num2)

n = 2
res = maxn * 2

while res % minn != 0:
    n = n + 1
    res = maxn * n

print(res)

#H
str = input()
num = int(input())

for i in range(num):
    print(str)

#I
num = int(input())
faq = 1

if num == 0:
    print(faq)
elif num > 0:
    for i in range(1, num + 1):
        faq = faq * i
    print(faq)

#J
vec = input()

x = 0
y = 0

while vec != 'СТОП':
    step = int(input())
    match vec:
        case 'СЕВЕР':
            y = y + step
        case 'ВОСТОК':
            x = x + step
        case 'ЗАПАД':
            x = x - step
        case 'ЮГ':
            y = y - step
    vec = input()

print(y, x, sep="\n")

#K
num = input()
i = 0
res = 0

while i < len(num):
    res = res + int(num[i])
    i = i + 1

print(res)

#L
num = input()
i = 0
max = num[i]
while i < len(num):
    if num[i] > max:
        max = num[i]
    i = i + 1

print(max)

#M
num = int(input())

for i in range(1, num + 1):
    name = input()
    if i == 1:
        res = name   
    elif name < res:
        res = name
    i = i + 1

print(res)

#N
n = int(input())
i, result = 2, 'YES'
if n > 1:
    while n % i:
        if i > n ** 0.5:
            break
        i += 1
    else:
        result = 'NO'
else:
    result = 'NO'
print(result)

#O
num = int(input())
n = 0

for i in range(num):
    name = input()
    if 'зайка' in name:
        n = n + 1
    i = i + 1

print(n)

#P
num = input()
num2 = ""
for i in range(len(num) - 1, -1, -1):
    num2 = num2 + num[i]

if num2 == num:
    print("YES")
else:
    print("NO")

#Q
num = input()
i = 0
res = ""

while i < len(num):
    if int(num[i]) % 2 != 0:
        res = res + num[i]
    i = i + 1

print(res)

#R
num = int(input())
i = 2
while num >= i:
    if num % i == 0:
        num = num / i
        print(f"{i}", end=" ")
        if num != 1:
            print("*", end=" ")
    else:
        i = i + 1

#S
step = num = 512                      
print(num)                            
while (text := input()) != "Угадал!": 
	step = round(step / 2)      
	if text == "Меньше":          
		num = num - step    
	if text == "Больше":       
		num = num + step     
	if num > 1000:               
		num = 1000           
	print(num)
        
#T
result, hn1 = -1, 0
for i in range(int(input())):
    b = int(input())
    h, r, m = b % 256, (b // 256) % 256, b // 256 ** 2
    t = ((m + r + hn1) * 37) % 256
    if t != h or h > 99:
        result = i
        break
    hn1 = h
print(result)