#A
print('Привет, Яндекс!')

#B
name = input("Как Вас зовут?")
print(f"Привет, {name}")

#C
text = input()
print(text)
print(text)
print(text)

#D
money = input()
print(int(int(money) - 2.5 * 38))

#E
price = float(input())
weight = float(input())
money = float(input())
change = money - price * weight
print(int(change))

#F
name = input()
price = float(input())
weight = float(input())
money = float(input())

iweight = int(weight)
iprice = int(price)

print("Чек")
print(f"{name} - {iweight}кг - {iprice}руб/кг")
print("Итого: ", int(weight * price), "руб", sep="")
print("Внесено: ", int(money), "руб", sep="")
change = money - price * weight
print("Сдача: ", int(change), "руб", sep="")

#G
num = int(input())
print("Купи слона!\n" * num)

#H
num = int(input())
line = input()
print(f'Я больше никогда не буду писать "{line}"!\n' * num)

#I
time = int(input())
kids = int(input())
onekid = int(time / 2)
print(onekid * kids)

#J
name = input()
num = input()

print(f"Группа №{num[0]}.")
print(f"{num[2]}. {name}.")
print(f"Шкафчик: {num}.")
print(f"Кроватка: {num[1]}.")

#K
num = input()
print(f"{num[1]}{num[0]}{num[3]}{num[2]}")

#L
num1 = f"{input():0>3}"
num2 = f"{input():0>3}"

res1 = str(int(num1[0]) + int(num2[0]))
res2 = str(int(num1[1]) + int(num2[1]))
res3 = str(int(num1[2]) + int(num2[2]))

print(int(f"{res1[-1]}{res2[-1]}{res3[-1]}"))

#M
kids = int(input())
sugars = int(input())

print(int(sugars / kids))
print(sugars % kids)

#N
red = int(input())
green = int(input())
blue = int(input())

print(red + blue + 1)

#O
hour = int(input())
minute = int(input())
delivery = int(input())

reshour = (hour + (minute + delivery) // 60) % 24
resmin = (minute + delivery) % 60

print(f"{reshour:0>2}:{resmin:0>2}")

#P
hour = int(input())
minute = int(input())
delivery = int(input())

reshour = (hour + (minute + delivery) // 60) % 24
resmin = (minute + delivery) % 60

print(f"{reshour:0>2}:{resmin:0>2}")

#Q
sum = int(input())
last = int(input(), 2)

print(sum + last)

#R
cost = int(input(), 2)
money = int(input())

print(money - cost)

#S
product = input()
cost = int(input())
weight = int(input())
money = int(input())

price = f"{weight}кг * {cost}руб/кг"
change = int(money - (cost * weight))
res = int(cost * weight)

print("================Чек================")
print("Товар:", f"{product:>28}")
print("Цена:", f"{price:>29}")
print("Итого:", f"{res:>25}руб")
print("Внесено:", f"{money:>23}руб")
print("Сдача:", f"{change:25}руб")
print("===================================")

#T
allN = int(input())
costM = int(input())
costK1 = int(input())
costK2 = int(input())

res2 = (allN * (costM - costK1)) // (costK2 - costK1)
res1 = allN - res2

print(res1, res2)