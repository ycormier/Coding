file = input("Which file would you like me to go through? >>>") + '.txt'
if len(file) < 5:
    file = 'clown.txt'

handle = open(file) # open the file that you want to read through

di = dict() # Create an empty dictionary to use later

for line in handle:
    line = line.strip() # divide text into separate lines
    word = line.split() # divide lines (above) into each word

for w in word:
    di[w] = di.get(w, 0) + 1

print(di)