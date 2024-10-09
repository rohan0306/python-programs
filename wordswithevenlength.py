n = 'This is a python language'
s = n.split(" ")            #split() the strings into list of words

for i in s:
    if len(i)%2 == 0:       ##it checks if it is even or not
        print(i, end=" ")   #print even words on a single line