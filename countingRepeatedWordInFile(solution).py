file = input("Which file would you like me to go through? >>>") + '.txt'
if len(file) < 5:
    file = 'clown.txt'

handle = open(file)  # open the file that you want to read through

di = dict()  # Create an empty dictionary to use later

for line in handle:
    line = line.strip()  # divide text into separate lines
    word = line.split()  # divide lines (above) into each word

for w in word:
    di[w] = di.get(w, 0) + 1  # going through each word and adding in to the dictionary
    # if the word is new, return 0 and then add 1
    # if the word is existing, return the amount of times that it exist and then add 1
    # the .get() does the counting for you

MostCommon = None  # Initiate the value for a counter that will give us the most common word
TimesInText = -1  # Initiating a value for the number of times it appears
# We cannot initiate the TimesInTest = None because None is it's own type of variable and we can't evaluate None > 'int'

for k, v in di.items():
    # .item() is the MOST important part here. It allows us to cycle through EACH key and EACH value
    if v > TimesInText:  # compares the value on the dictionary to the existing value
        TimesInText = v
        # if the value in the dict is higher than the one the variable it replaces it
        MostCommon = k
        # The key associated to the value above also replaces the variable the one in our variable "MostCommon"

print(f"The most common word is ...{MostCommon}... and it appears {TimesInText} times")
