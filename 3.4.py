#A
for index, value in enumerate(input().split(), 1):
    print(f"{index}. {value}")

#B
first = input().split(", ")
second = input().split(", ")
for i in zip(first, second):
    print(" - ".join(i))

#C
from itertools import count

text = list(map(float, input().split()))
for i in count(text[0], text[2]):
    if i <= text[1]:
        print(round(i, 2))
    else:
        break

#blablabla

#D
from itertools import accumulate

text = [str(i) + " " for i in input().split()]
for i in accumulate(text):
    print(i)

#E
from itertools import count

arr = [j for i in range(3) for j in input().split(", ")]
for i, j in enumerate(sorted(arr), 1):
    print(f"{i}. {j}")

#F
from itertools import product

text = input()
masti = ["пик", "треф", "бубен", "червей"]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]
for i in list(product(cards, masti)):
    if i[1] != text:
        print(i[0], i[1])

#G
from itertools import combinations

num = int(input())
arr = [input() for i in range(num)]
res = list(combinations(arr, 2))
for i in res:
    print(f"{i[0]} - {i[1]}")

#H
from itertools import cycle

num = int(input())
arr = [input() for i in range(num)]
days = int(input())
res = []
for j in cycle(arr):
    if len(res) < days:
        res.append(j)
    else:
        break
[print(k) for k in res]

#I
from itertools import product

num = int(input())
arr = [i for i in range(1, num + 1)]
flag = 0
for i in product(arr, arr):
    print(i[0] * i[1], end=" ")
    flag += 1
    if flag % num == 0:
        print()

#J
from itertools import product

num = int(input())
print("А", "Б", "В")
for i in product(range(1, num + 1), range(1, num + 1), range(1, num + 1)):
    if sum(i) == num:
        print(i[0], i[1], i[2])

#K
from itertools import product

num1 = int(input())
num2 = int(input())
count = 0
leng = len(str(num1 * num2))
for i in product(range(1, num1 + 1), range(1, num2 + 1)):
    count += 1
    print(f"{count:>{leng}}", end=" ")
    if count % num2 == 0:
        print()

#L
num = int(input())
arr = []
for i in range(num):
    arr.extend(input().split(", "))
for index, value in enumerate(sorted(arr), 1):
    print(f"{index}. {value}")

#M
from itertools import permutations

num = int(input())
arr = list(permutations(sorted([input() for i in range(num)])))
for i in arr:
    print(", ".join(i))

#N
from itertools import permutations

num = int(input())
arr = list(permutations(sorted([input() for i in range(num)]), r=3))
for i in arr:
    print(", ".join(i))

#O
from itertools import permutations

num = int(input())
arr = []
[arr.extend(input().split(", ")) for i in range(num)]
for i in permutations(sorted(arr), r=3):
    print(" ".join(i))

#P
from itertools import product, combinations

mast = input()
delete = input()

karti = sorted([str(i) for i in range(2, 11)])
karti.extend(["валет", "дама", "король", "туз"])
karti.remove(delete)
masti = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
arr = product(karti, masti.values())
count = 0
for i in list(combinations(arr, 3)):
    if i[0][1] == masti.get(mast) or i[1][1] == masti.get(mast) or i[2][1] == masti.get(mast):
        count += 1
        print(", ".join([f"{k} {j}" for k, j in i]))
    if count == 10:
        break

#Q
from itertools import product, combinations

mast = input()
delete = input()
vital = input()

flag = False
karti = sorted([str(i) for i in range(2, 11)])
karti.extend(["валет", "дама", "король", "туз"])
karti.remove(delete)
masti = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
arr = product(karti, masti.values())
for i in list(combinations(arr, 3)):
    if i[0][1] == masti.get(mast) or i[1][1] == masti.get(mast) or i[2][1] == masti.get(mast):
        string = ", ".join([f"{k} {j}" for k, j in i])
        if string == vital:
            flag = True
            continue
        if flag:
            print(string)
            break

#R
from itertools import product

string = tuple(input().split())
arr = (list(product("01", repeat=3)))
print("a b c f")
for i in arr:
    copy = []
    for j in string:
        if j == "a":
            copy.append(i[0])
        elif j == "b":
            copy.append(i[1])
        elif j == "c":
            copy.append(i[2])
        else:
            copy.append(j)
    copy = " ".join(copy)
    print(*i, int(eval(copy)))

#S
from itertools import product

string = input()
vars = sorted(set([i for i in string.split() if i.isupper()]))
arr = list(product("01", repeat=len(vars)))
print(" ".join(vars), "F")
for i in arr:
    dict = {}
    count = 0
    for j in vars:
        dict[j] = int(i[count])
        count += 1
    print(*i, int(eval(string, dict)))

#T
from itertools import product

OPERATORS = {
    'not': 'not',
    'and': 'and',
    'or': 'or',
    '^': '!=',
    '->': '<=',
    '~': '==',
}

PRIORITY = {
    'not': 0,
    'and': 1,
    'or': 2,
    '^': 3,
    '->': 4,
    '~': 5,
    '(': 6,
}


def postfix_expression(expression, variables):
    stack, result, lst = [], [], expression.split()
    for i in lst:
        if i in variables:
            result.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                result.append(OPERATORS[stack.pop()])
            stack.pop()
        elif i in OPERATORS.keys():
            while len(stack) and PRIORITY[i] >= PRIORITY[stack[-1]]:
                result.append(OPERATORS[stack.pop()])
            stack.append(i)
    for _ in range(len(stack)):
        result.append(OPERATORS[stack.pop()])
    return result


def result_of_expression(postfix_exp, variables):
    stack = []
    for i in range(len(postfix_exp)):
        if postfix_exp[i] in variables.keys():
            stack.append(variables[postfix_exp[i]])
        else:
            if postfix_exp[i] == 'not':
                stack.append(not stack.pop())
            else:
                var2, var1 = stack.pop(), stack.pop()
                stack.append(eval(f'{var1} {postfix_exp[i]} {var2}'))
    return int(stack.pop())


statement = input()
var_all = sorted(set([i for i in statement if i.isupper()]))
print(' '.join(var_all), 'F')
table = product([0, 1], repeat=len(var_all))
statement = statement.replace('(', '( ').replace(')', ' )')
exp = postfix_expression(statement, var_all)

for row in table:
    res = {}
    for k, v in zip(var_all, row):
        res[k] = v
    print(' '.join(str(x) for x in row), result_of_expression(exp, res))