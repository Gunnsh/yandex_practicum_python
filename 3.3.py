#A
[i ** 2 for i in range(a, b + 1)]

#B
[[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]

#C
[[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]

#D
{i for i in numbers if i % 2 != 0}

#E
{i for i in numbers if pow(i, 0.5) % 1 in [0.0, 1.0]}

#F
{i: text.lower().count(i) for i in set(text.lower()) if i.isalpha()}

#G
{i: [j for j in range(1, i + 1) if i % j == 0] for i in numbers}

#H
"".join([i[0].upper() for i in string.split()])

#I
" - ".join([str(i) for i in sorted(list(set(numbers)))])

#J
"".join([i[0] * i[1] for i in rle])