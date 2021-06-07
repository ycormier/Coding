a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

c = int(input("Please provide a number: "))

b = []
for num in a:
    if num < c:
        b.append(num)
print(b)
# Same above an below #
d = [num for num in a if num < c]
print(d)
