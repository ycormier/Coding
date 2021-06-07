from random import randint
y = []
z = []

i = 0
x = randint(1, 10)
while i < x:
    y.append(randint(0, 100))
    z.append(randint(0, 100))
    i += 1
print(x)
print(y)
print(z)

compare = [val for val in y if val in z]
print(compare)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
comp = (set(a) & set(b))
print(list(comp))
