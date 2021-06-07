num = int(input("Please provide a number: "))
x = range(1, num+1)
z = []
for value in x:
    if num % value == 0:
      z.append(value)
print(z)
# OR #
# make sure that you put the [] in the print statement of it will create a '<generator object <genexpr> at 0x000....'
print([value for value in x if num % value == 0])
