a = [9, 41, 12, 3, 74, 15]
largest = None

print("Begin")
for num in a:
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    print(largest, num)
print(f"The largest number in the list is {largest}")
