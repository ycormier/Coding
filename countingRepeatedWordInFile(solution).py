file = input("Which file would you like me to go through? >>>") + '.txt'
if len(file) < 5:
    file = 'clown.txt'

handle = open(file)

for line in handle:
    line = line.strip()
    word = line.split()

